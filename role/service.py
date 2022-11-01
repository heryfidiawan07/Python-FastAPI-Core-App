from fastapi import Depends
from sqlalchemy.orm import joinedload
from config.database import db
from role.model import RoleModel
from permission.model import RolePermissionModel
from uuid import UUID

class RoleService():

    def all():
        return db.query(RoleModel).all()
    
    def find(id: UUID):
        return db.query(RoleModel).options(joinedload(RoleModel.users), joinedload(RoleModel.permissions)).get(id)
    
    def destroy(id: UUID):
        try:
            model = db.query(RoleModel).get(id)
            if model is None:
                raise HTTPException(status_code=404, detail="Data not found")

            db.delete(model)
            db.commit()
            db.close()
        except Exception as error:
            raise HTTPException(status_code=500, detail="Internal server error")
    
    def create(request: any):
        try:
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
        except Exception as error:
            raise HTTPException(status_code=500, detail="Internal server error")
    
    def edit(id: UUID, request: any):
        try:
            model = db.query(RoleModel).get(id)
            if model is None:
                raise HTTPException(status_code=404, detail="Data not found")

            model.name = request.name,
            db.commit()
            db.refresh(model)
            return user
        except Exception as error:
            raise HTTPException(status_code=500, detail="Internal server error")