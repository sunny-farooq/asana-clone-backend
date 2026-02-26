from helpers.user_helper import read_current_user
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from models.portfolio import portfolio
from models.account import account


portfolio_router = APIRouter(tags=["Portfolio"])

@portfolio_router.get("/get-portfolios-for-current-users")
async def portfolio_current_user(user: Annotated[account, Depends(read_current_user)]):
    try:
        user_id = user.id
        portfolio_of_user = await portfolio.get_or_none(owner_id=user_id)
        return portfolio_of_user
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))



@portfolio_router.post("/create_portfolio")
async def create_portfolio(name: str,user: Annotated[account, Depends(read_current_user)]):
    user_id = user.id
    user_org = user.organization_id
    try:
        await portfolio.create(organization_id=user_org,owner_id=user_id,name=name,status="ongoing")
        return {"status": "Project created Successfully"}
    except Exception as e:
        return {"status":"Error Occurred"}
        






