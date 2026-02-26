from helpers.user_helper import read_current_user
from fastapi import APIRouter, Depends, HTTPException
from models.account import account
from models.task import task
from models.task_like import task_like
from typing import Annotated
from pydantic import BaseModel
from models.project import project


task_router = APIRouter(tags=['Tasks'])

class task_to_be_created(BaseModel):
    category: str
    assign_date: str
    due_date: str
    priority: str
    status: str
    

@task_router.post("/create-task")
async def create_task(request: task_to_be_created, user: Annotated[account, Depends(read_current_user)]):
    try:
        org_id = user.organization_id
        projected = await project.get_or_none(organization_id=org_id)  
        create_task = await task.create(category=request.category,assign_date=request.assign_date,due_date=request.due_date, priority=request.priority, status=request.status,assignee_id=str(user.id),project_id=str(projected.id))
        return create_task
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@task_router.post("/like_task")
async def like_task(task_id:str,user: Annotated[account, Depends(read_current_user)]):
    try:
        user_id = user.id
        await task_like.create(account_id=user_id,task_id=task_id)
        return {"status": "task_liked"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    