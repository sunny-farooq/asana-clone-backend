from helpers.user_helper import read_current_user
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from models.account import account
from models.goal import goal
from models.goal_projects import goal_projects
from models.goal_tasks import goal_tasks

goal_router = APIRouter(tags=["Goals"])

@goal_router.post("/create-goals")
async def create_goals(title:str,user: Annotated[account,Depends(read_current_user)]):
    try:
        user_id = user.id
        user_org = user.organization_id
        await goal.create(title=title, owner_id=user_id, organization_id=user_org)
        return {"status":"goal created"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@goal_router.post("/add-project-in-goal")
async def add_projects(projectid: str,goalid:str, user: Annotated[account,Depends(read_current_user)]):
    try:
        await goal_projects.create(goal_id=goalid,project_id=projectid)
        return {"status":"project added in Goal"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@goal_router.post("/add-tasks-in-goal")
async def add_tasks(taskid: str, goalid:str, user: Annotated[account, Depends(read_current_user)]):
    try:
        user_id=user.id
        await goal_tasks.create(goal_id=goalid,task_id=taskid)
        return {"status":"Tasks Added in the Goal"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))