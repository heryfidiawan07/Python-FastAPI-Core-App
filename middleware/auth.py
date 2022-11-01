from fastapi import Header, HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError
from jose import JWTError, jwt
from config.database import db
from user.model import UserModel
from helper.token import get_current_user

class Auth():

    async def check(access_token: str | None = Header(default=None)):
        SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
        if not access_token:
            raise HTTPException(status_code=401, detail="Unauthorized")
        try:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(status_code=401, detail="Unauthorized")
            return username
        except JWTError:
            raise HTTPException(status_code=401, detail="Unauthorized")

    def permissions():
        return True
        