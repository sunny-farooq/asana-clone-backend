from helpers.user_helper import read_current_user
from fastapi import APIRouter, Depends
from models.account import account
from typing import Annotated
from models.project import project


project_router = APIRouter(tags=["Projects"])

@project_router.post("/create_project")
async def create_project(user: Annotated[account,Depends(read_current_user)],project_name:str):
    org_id = user.organization_id
    new_project = await project.create(name=project_name, status="Ongoing", organization_id=org_id)
    return {"status":"Project Creation Successful","project_name":project_name}


@project_router.post("/update_project_status")
async def update(user: Annotated[account,Depends(read_current_user)], status:str):
    org_id = user.organization_id
    new_status = await project.filter(organization_id=org_id).update(status=status)
    return {"status":f"Project Status set to {status}"}


@project_router.post("/update_project_name")
async def update_name(user: Annotated[account,Depends(read_current_user)], name:str):
    org_id = user.organization_id
    new_status = await project.filter(organization_id=org_id).update(name=name)
    return {"status":f"Project Name set to {name}"}