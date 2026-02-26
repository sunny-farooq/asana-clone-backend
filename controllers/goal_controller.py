from helpers.user_helper import read_current_user
from fastapi import APIRouter, Depends
from typing import Annotated
from models.account import account
from models.goal import goal


goal_router = APIRouter(tags=["Goals"])

@goal_router.post("/create-goals")
async def create_goals(title:str,user: Annotated[account,Depends(read_current_user)]):
    user_id = user.id
    user_org = user.organization_id
    await goal.create(title=title, owner_id=user_id)