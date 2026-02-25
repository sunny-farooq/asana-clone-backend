import jwt
from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException
from models.account import account
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY=os.getenv("ADMIN_SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")

security = HTTPBearer()

async def read_current_user(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)]):
    try:
       payload =  decode_token(credentials.credentials)
       user = await account.get_or_none(id=payload.get("user_id", None))
       if not user:
          raise HTTPException("User not found")
       return user
    except Exception as e:
       raise HTTPException(f" Error: {e}")


def create_access_token(payload: dict):
    return jwt.encode(payload, SECRET_KEY, ALGORITHM)

def decode_token(jwt_token: str):
    return jwt.decode(jwt_token,SECRET_KEY, ALGORITHM)

if __name__ == "__main__":
 create_access_token({"user_id":1})