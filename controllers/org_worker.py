from fastapi import APIRouter, HTTPException, Depends
from models.account import account
from models.organization import organization
from models.organization_member import organization_member
from helpers.user_helper import read_current_user
from typing import Annotated
from helpers.invitation_code_helper import invitation_code_generator
from helpers.iso_time_helper import iso_time
from argon2 import PasswordHasher

ph = PasswordHasher()

org_worker = APIRouter(tags=["Add User to Organization"])

@org_worker.post("/invite-user-to-organization")
async def invite_user(organization_id:str,email:str,user: Annotated[account, Depends(read_current_user)]):
    user_id = user.id
    orgs_of_user = await organization.filter(participant_id=user_id).all().values_list("id", flat=True)
    invitation_code = invitation_code_generator()
    org_ids_as_strings = [str(org_id) for org_id in orgs_of_user]
    try:
        if organization_id in org_ids_as_strings:
            return await organization_member.create(role='user',
                                            organization_id=organization_id,email=email,
                                            invitation_code=invitation_code,invited_at=iso_time()) 
    except Exception as e:
        raise HTTPException(status_code=401,detail="User not found")


@org_worker.post("/accept-invite")
async def accept_invite(invitation_code:str, password:str,name:str):
    invited_user = await organization_member.get_or_none(invitation_code=invitation_code)
    if not invite_user:
        raise HTTPException(status_code=404,detail="Invitation not found")
    invited_user_email = invited_user.email
    invited_org = invited_user.organization_id
    hashed_password = ph.hash(password)
    new_user = await account.create(email=invited_user_email,
                                    name=name,
                                    password=hashed_password,
                                    is_verified=True,
                                    role='user',
                                    organization_id=invited_org)
    return new_user

# @org_worker.post("/invite-user-to-organization")
# async def invite_user(
#     organization_id: str,email: str, user: Annotated[account, Depends(read_current_user)]
# ):
#     # 1. Fetch only the IDs of organizations this user belongs to
#     # .values_list("id", flat=True) returns a simple list like ["id1", "id2"]
#     user_org_ids = await organization.filter(participant_id=user.id).all().values_list("id", flat=True)

#     # 2. Check if the requested organization_id is in that list
#     if organization_id not in user_org_ids:
#         raise HTTPException(
#             status_code=403, 
#             detail="You do not have permission to invite users to this organization."
#         )

#     # 3. If check passes, proceed with creating the invitation
#     invitation_code = invitation_code_generator()
#     try:
#         await organization_member.create(
#             organization_id=organization_id,
#             email=email,
#             invitation_code=invitation_code,
#             invited_at=iso_time()
#         )
#         return {"status": "success", "message": "Invitation sent"}
#     except Exception as e:
#         # It's better to log the error 'e' here for debugging
#         raise HTTPException(status_code=500, detail="Internal server error while creating invitation")
        
