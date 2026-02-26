from helpers.user_helper import read_current_user
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from models.comment import comment
from models.task import task
from models.account import account



comment_router = APIRouter(tags=["Comments"])


@comment_router.post("/comment")
async def add_comment(task_id: str, comment_text:str,user: Annotated[account, Depends(read_current_user)]):
    try:
        user_id = user.id
        await comment.create(task_id=task_id,account_id=user_id,comment_text=comment_text)
        return {"status":"comments Added"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@comment_router.patch("/comment-patch")
async def change_comment(comment_id: str, update_text:str,user: Annotated[account, Depends(read_current_user)]):
    try:
        await comment.filter(id=comment_id).update(comment_text=update_text)
        return {"status":"comments updated"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


