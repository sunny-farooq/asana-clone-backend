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
        await goal_tasks.create(goal_id=goalid,task_id=taskid)
        return {"status":"Tasks Added in the Goal"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@goal_router.delete("/remove-project-from-goal")
async def remove_project_from_goal(projectid: str,goalid:str, user: Annotated[account,Depends(read_current_user)]):
    try:
        project_to_remove = await goal_projects.filter(goal_id=goalid,project_id=projectid)
        await project_to_remove.delete()
        return {"status":"project removed from Goal"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@goal_router.delete("/remove-task-from-goal")
async def remove_task_from_goal(taskid: str, goalid:str, user: Annotated[account, Depends(read_current_user)]):
    try:
        task_to_remove=await goal_tasks.filter(goal_id=goalid,task_id=taskid)
        await task_to_remove.delete()
        return {"status":"Tasks removed from the Goal"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@goal_router.patch("/update_goal")
async def update_goal(goalid:str, new_title:str, user: Annotated[account, Depends(read_current_user)]):
    try:
        updated_goal = await goal.filter(id=goalid).update(title=new_title)
        return updated_goal
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@goal_router.delete("/delete-goal")
async def delete_goal(goalid:str, user: Annotated[account, Depends(read_current_user)]):
    try:
        deleted_goal = await goal.filter(id=goalid)
        deleted_goal.delete()
        return {"status":"status deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@goal_router.get("/get-goal")
async def get_goal(goalid:str, user: Annotated[account, Depends(read_current_user)]):
    try:
        get_goal = await goal.get_or_none(id=goalid)
        return get_goal
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@goal_router.get("/get-all-goals")
async def get_all_goals(user: Annotated[account, Depends(read_current_user)]):
    try:
        owner_id = user.id
        all_goal = await goal.filter(owner_id=owner_id).all()
        return all_goal
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))