from fastapi import Depends
from sqlalchemy.orm import joinedload
from config.database import db
from user.model import UserModel
from helper.bcrypt import Hash

class UserService():

    def all():
        return db.query(UserModel).all()
    
    def find(id: str):
        # db.query(UserModel).filter(UserModel.username == username).first()
        # db.query(UserModel).offset(skip).limit(limit).all()
        return db.query(UserModel).options(joinedload(UserModel.role)).get(id)
    
    def destroy(id: str):
        model = db.query(UserModel).get(id)
        db.delete(model)
        db.commit()
        db.close()
    
    def create(request: any):
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
    
    def edit(id: str, request: any):
        model = db.query(UserModel).get(id)
        model.name = request.name,
        model.username = request.username,
        model.email = request.email,
        model.role_id = request.role_id,
        db.commit()
        db.refresh(model)
        return user