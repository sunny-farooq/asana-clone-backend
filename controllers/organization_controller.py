from fastapi import APIRouter, HTTPException, Depends
from models.organization import organization
from helpers.user_helper import read_current_user
from typing import Annotated
from pydantic import BaseModel
from models.account import account
from datetime import date

class card_details(BaseModel):
    card_number: str
    exp_date: int
    card_cvv: int

organization_router = APIRouter(tags=["Organization"])

@organization_router.patch("/update_organization")
async def update_organization(user: Annotated[account,Depends(read_current_user)],new_name:str):
    
    try:
        org_id = user.organization_id
        await organization.filter(id=org_id).update(name=new_name)
        return {"new_name": new_name}
    except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))

@organization_router.post("/add_card")
async def add_card(user: Annotated[account,Depends(read_current_user)], request: card_details):
    try:
        org_id = user.organization_id
        await organization.filter(id=org_id).update(card_number=request.card_number, card_expiry=request.exp_date, card_cvv=request.card_cvv)
        return {"status":"updated"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@organization_router.post("/activate_trial")
async def activate_trial(user: Annotated[account,Depends(read_current_user)]):
    try:
        day_today = date.today()
        org_id = user.organization_id
        await organization.filter(id=org_id).update(trial_status="Activated", billing_date=day_today)
        return {"status":"trial activated"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@organization_router.post("/new_organization")
async def create_new_organization(name:str, user: Annotated[account,Depends(read_current_user)]):
    try:
        new_org=await organization.create(name=name)
        return new_org
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))
    
@organization_router.get("/get_organization")
async def get_organization(org_id:str, user: Annotated[account,Depends(read_current_user)]):
    try:
        org = await organization.get_or_none(id=org_id)
        return org
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))
    
@organization_router.delete("/delete_organization")
async def delete_organization(org_id:str, user: Annotated[account, Depends(read_current_user)]):
    try:
        org_to_delete = await organization.filter(id=org_id).all()
        await org_to_delete.delete()
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))