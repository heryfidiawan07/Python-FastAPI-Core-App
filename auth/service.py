from fastapi import Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from config.database import db
from user.model import UserModel
from role.model import RoleModel
from helper.bcrypt import Hash, Verify
from helper.token import create_access_token, get_current_user
from datetime import datetime, timedelta

class AuthService():

    def login(request: any):
        user = db.query(UserModel).filter(UserModel.username == request.username).first()
        if user is None:
            raise HTTPException(status_code=404, detail="Data not found")

        if not Verify(request.password, user.password):
            raise HTTPException(status_code=404, detail="Invalid credentials")
        
        token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=token_expires
        )
        refresh_token = create_access_token(
            data={"sub": user.username}, expires_delta=token_expires * 2
        )

        return {
            "access_token": {
                "type": "bearer",
                "token": access_token,
            }, 
            "refresh_token": refresh_token 
        }
    
    def register(request: any):
        try:
            role = db.query(RoleModel).filter(RoleModel.name == "Guest").first()
            if role is None:
                raise HTTPException(status_code=404, detail="Role guest not found")

            valid = UserModel(
                name = request.name,
                username = request.username,
                email = request.email,
                password = Hash(request.password),
                role_id = role.id
            )
            db.add(valid)
            db.commit()
            db.refresh(valid)
            return valid
        except SQLAlchemyError as error:
            raise HTTPException(status_code=500, detail="Internal server error")
    
    def me(token: str):
        try:
            return get_current_user(token)
        except SQLAlchemyError as error:
            raise HTTPException(status_code=500, detail="Internal server error")