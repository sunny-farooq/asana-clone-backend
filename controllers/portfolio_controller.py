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
        portfolio_of_user = await portfolio.filter(owner_id=user_id).all()
        return portfolio_of_user
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))



@portfolio_router.post("/create_portfolio")
async def create_portfolio(name: str,user: Annotated[account, Depends(read_current_user)]):
    user_id = user.id
    user_org = user.organization_id
    try:
        await portfolio.create(organization_id=user_org,owner_id=user_id,name=name,status="ongoing")
        return {"status": "Portfolio created Successfully"}
    except Exception as e:
        return {"status":"Error Occurred"}
    
@portfolio_router.get("/get-portfolio")
async def get_portfolio(portfolio_id:str, user: Annotated[account, Depends(read_current_user)]):
    try:
        portfolio_needed = await portfolio.get_or_none(id=portfolio_id)
        return portfolio_needed
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))

@portfolio_router.patch("/update_portfolio")
async def update_portfolio(portfolio_id:str, name:str, user: Annotated[account, Depends(read_current_user)]):
    try: 
        await portfolio.filter(id=portfolio_id).update(name=name)
        return {"status":f"name set to {name} successfully of your portfolio"}
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    
@portfolio_router.delete("/delete_portfolio")
async def delete_portfolio(portfolio_id:str, user: Annotated[account,Depends(read_current_user)]):
    try:
        delete_portfolio = await portfolio.get_or_none(id=portfolio_id)
        await delete_portfolio.delete()
        return {"status":"Portfolio Deleted Successfully"}
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))






