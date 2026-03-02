from helpers.user_helper import read_current_user
from fastapi import APIRouter, Depends, HTTPException
from models.account import account
from typing import Annotated
from models.project import project


project_router = APIRouter(tags=["Projects"])

@project_router.get("/list_projects")
async def list_projects(org_id:str, user: Annotated[account,Depends(read_current_user)]):
    try:
        all_projects = await project.filter(organization_id=org_id).all()
        return all_projects
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@project_router.get("/get-project")
async def get_project(project_id:str,user: Annotated[account,Depends(read_current_user)]):
    try: 
        project_wanted = await project.get_or_none(id=project_id)
        return project_wanted
    except Exception as e:
        raise HTTPException(status=404, details=str(e))

@project_router.post("/create_project")
async def create_project(orgid:str,user: Annotated[account,Depends(read_current_user)],project_name:str):
    try:
        new_project = await project.create(name=project_name, status="Ongoing", organization_id=orgid)
        return new_project
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@project_router.patch("/update_project_status")
async def update(orgid: str,projid:str,user: Annotated[account,Depends(read_current_user)], status:str):
    try:
        await project.filter(organization_id=orgid,id=projid).update(status=status)
        return {"status":f"Project Status set to {status}"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@project_router.patch("/update_project_name")
async def update_name(orgid: str,projid:str,user: Annotated[account,Depends(read_current_user)], name:str):
    try:
        await project.filter(organization_id=orgid,id=projid).update(name=name)
        return {"status":f"Project Name set to {name}"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@project_router.delete("/delete_project")
async def delete_project(project_id:str, user: Annotated[account,Depends(read_current_user)]):
    try:
        await project.filter(id=project_id).delete()
        return {"status":"Project deleted"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))