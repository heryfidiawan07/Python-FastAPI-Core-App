from fastapi import Depends, HTTPException
from sqlalchemy.orm import joinedload
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from config.database import db
from user.model import UserModel
from permission.model import PermissionModel
from datetime import datetime, timedelta

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Unauthorized")
    except JWTError:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user = db.query(UserModel).options(joinedload(UserModel.role)).filter(UserModel.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    permissions_id = []
    for x in user.role.permissions:
        permissions_id.append(x.permission_id)

    permissions = db.query(PermissionModel).options(joinedload(PermissionModel.menu)).filter(PermissionModel.id.in_(permissions_id)).all()

    permissions_name = []
    for x in permissions:
        permissions_name.append(x.name)

    return {"user": user, "menu": permissions, "permissions": permissions_name}
    # return user
