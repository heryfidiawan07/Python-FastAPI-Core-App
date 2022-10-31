from fastapi import Depends
from sqlalchemy.orm import joinedload
from config.database import db
from role.model import RoleModel
from permission.model import RolePermissionModel

class RoleService():

    def all():
        return db.query(RoleModel).all()
    
    def find(id: str):
        return db.query(RoleModel).options(joinedload(RoleModel.users), joinedload(RoleModel.permissions)).get(id)
    
    def destroy(id: str):
        model = db.query(RoleModel).get(id)
        db.delete(model)
        db.commit()
        db.close()
    
    def create(request: any):
        role = RoleModel(
            name = request.name,
        )
        rolePermission = RolePermissionModel(
            role_id = request.name,
        )
        db.add(role)
        db.commit()
        # role permissions
        objects = []
        for permission in request.permission_id:
            dbitem = RolePermissionModel(
                role_id = role.id,
                permission_id = permission,
            )
            objects.append(dbitem)
        # save role permissions
        db.bulk_save_objects(objects)
        db.commit()
        # 
        db.refresh(role)
        return role
    
    def edit(id: str, request: any):
        model = db.query(RoleModel).get(id)
        model.name = request.name,
        db.commit()
        db.refresh(model)
        return user