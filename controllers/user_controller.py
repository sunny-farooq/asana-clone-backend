from fastapi import APIRouter, HTTPException
from models.account import account
from models.organization import organization
from models.organization_member import organization_member
from argon2 import PasswordHasher
from helpers.user_helper import create_access_token
from pydantic import BaseModel

ph = PasswordHasher()

class signup(BaseModel):
    name: str
    email: str
    password: str

user_router = APIRouter(tags = ["User"])

@user_router.get("/")
def what():
    return {"status": "admin_router is Working Properly"}

@user_router.post("/signup")
async def user_signup(request: signup):
    organization_name = f"The {request.name}'s Organization"
    check_before = await account.filter(email=request.email)
    if check_before:
        raise HTTPException(status_code=409,detail= "Email Already in use")
    try:
        new_organization = await organization.create(name=organization_name)
        hashed_password=ph.hash(request.password)   
        new_user = await account.create(name=request.name,email=request.email,password=hashed_password,role="owner",organization_id=new_organization.id)
        new_org_member = await organization_member.create(role="owner", account_id=new_user.id, organization_id=new_organization.id  )
        return {"name": new_user.name, "email": request.email, "Organization_name": organization_name, "organization_member_id": new_org_member.id }
    except Exception as e:
        raise HTTPException(401, str(e))

@user_router.get("/login")
async def login(email: str, password: str):
    try:
        user = await account.get_or_none(email=email)
        if not ph.verify(user.password,password):
            raise HTTPException(status_code=405,details= "Password Doesn't match")
        token=create_access_token({"user_id": str(user.id), "email": user.email})
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=405,detail= "Wrong Password")


