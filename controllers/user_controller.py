from fastapi import APIRouter, HTTPException, Depends
from models.account import account
from models.organization import organization
from models.organization_member import organization_member
from argon2 import PasswordHasher
from helpers.user_helper import create_access_token, read_current_user
from pydantic import BaseModel, EmailStr
from typing import Annotated


ph = PasswordHasher()

class signup(BaseModel):
    name: str
    email: EmailStr
    password: str

class Login(BaseModel):
    email: EmailStr
    password: str

user_router = APIRouter(tags = ["User"])



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

@user_router.post("/login")
async def login(request: Login):
    try:
        user = await account.get_or_none(email=request.email)
        if not ph.verify(user.password,request.password):
            raise HTTPException(status_code=405,details= "Password Doesn't match")
        token=create_access_token({"user_id": str(user.id), "email": user.email})
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=405,detail= "Wrong Password")
    
@user_router.get("/get-user")
async def get_user(user: Annotated[account,Depends(read_current_user)]):
    return user

@user_router.patch("/update-user")
async def update_user(name: str,user: Annotated[account,Depends(read_current_user)]):
    await account.filter(id=user.id).update(name=name)
    updated_user = await account.get_or_none(id=user.id)
    return updated_user

@user_router.delete("/delete-user")
async def delete_user(user: Annotated[account,Depends(read_current_user)]):
    user_to_delete = await account.get_or_none(email=user.email)
    await user_to_delete.delete()
    return {"status":"User Deleted"}