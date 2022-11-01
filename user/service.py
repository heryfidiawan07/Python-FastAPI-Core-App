from fastapi import Depends, HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError
from config.database import db
from user.model import UserModel
from helper.bcrypt import Hash
from uuid import UUID

class UserService():

    def all():
        # db.query(UserModel).filter(UserModel.username == username).first()
        # db.query(UserModel).offset(skip).limit(limit).all()
        return db.query(UserModel).all()
    
    def find(id: UUID):
        return db.query(UserModel).options(joinedload(UserModel.role)).get(id)
    
    def destroy(id: UUID):
        try:
            model = db.query(UserModel).get(id)
            if model is None:
                raise HTTPException(status_code=404, detail="Data not found")

            db.delete(model)
            db.commit()
            db.close()
        except SQLAlchemyError as error:
            raise HTTPException(status_code=500, detail="Internal server error")
    
    def create(request: any):
        try:
            valid = UserModel(
                name = request.name,
                username = request.username,
                email = request.email,
                password = Hash(request.password),
                role_id = request.role_id
            )
            db.add(valid)
            db.commit()
            db.refresh(valid)
            return valid
        except SQLAlchemyError as error:
            raise HTTPException(status_code=500, detail="Internal server error")
    
    def edit(id: UUID, request: any):
        try:
            model = db.query(UserModel).get(id)
            if model is None:
                raise HTTPException(status_code=404, detail="Data not found")

            model.name = request.name,
            model.username = request.username,
            model.email = request.email,
            model.role_id = request.role_id,
            db.commit()
            db.refresh(model)
            return user
        except SQLAlchemyError as error:
            raise HTTPException(status_code=500, detail="Internal server error")