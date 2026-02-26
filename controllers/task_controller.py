from helpers.user_helper import read_current_user
from fastapi import APIRouter, Depends
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


@task_router.post("/tasks-health")
def tasks_health():
    return "hello"


@task_router.post("/create-task")
async def create_task(request: task_to_be_created, user: Annotated[account, Depends(read_current_user)]):
    org_id = user.organization_id
    projected = await project.get_or_none(organization_id=org_id)  
    create_task = await task.create(category=request.category,assign_date=request.assign_date,due_date=request.due_date, priority=request.priority, status=request.status,assignee_id=str(user.id),project_id=str(project.id))
    return create_task

@task_router.post("/like_task")
async def like_task(task_id:str,user: Annotated[account, Depends(read_current_user)]):
    user_id = user.id
    await task_like.create(account_id=user_id,task_id=task_id)
    return {"status": "task_liked"}
    