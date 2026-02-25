from fastapi import APIRouter, HTTPException, Depends
from models.organization import organization
from helpers.user_helper import read_current_user
from typing import Annotated
from pydantic import BaseModel
from models.account import account
from datetime import date

class card_details(BaseModel):
    card_number: int
    exp_date: int
    card_cvv: int

organization_router = APIRouter(tags=["Organization"])

@organization_router.get("/organization-health")
def health():
    return "Good Health"

@organization_router.post("/change_name")
async def org_name_change(user: Annotated[account,Depends(read_current_user)],new_name:str):
    org_id = user.organization_id
    org = await organization.filter(id=org_id).update(name=new_name)
    return {"new_name": new_name}

@organization_router.post("/add_card")
async def add_card(user: Annotated[account,Depends(read_current_user)], request: card_details):
    org_id = user.organization_id
    org_details = await organization.filter(id=org_id).update(card_number=request.card_number, card_expiry=request.exp_date, card_cvv=request.card_cvv)
    return {"status":"updated"}


@organization_router.post("/activate_trial")
async def activate_trial(user: Annotated[account,Depends(read_current_user)]):
    day_today = date.today()
    org_id = user.organization_id
    activate_in_db = await organization.filter(id=org_id).update(trial_status="Activated", billing_date=day_today)
    return {"status":"trial activated"}

