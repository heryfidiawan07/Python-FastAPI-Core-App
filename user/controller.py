from fastapi import APIRouter, Depends, HTTPException, Header
from middleware.auth import Auth
from user.model import UserModel
from user.service import UserService
from user.request import UserCreate, UserUpdate
from uuid import UUID

router = APIRouter()

@router.get("/user", dependencies=[Depends(Auth.check)])
async def index():
    return UserService.all()

@router.get("/user/{id}")
async def show(id: UUID):
    return UserService.find(id)

@router.delete("/user/{id}")
async def delete(id: UUID):
    UserService.destroy(id)
    return "Data was deleted"

@router.post("/user")
async def store(request: UserCreate):
    return UserService.create(request)

@router.put("/user/{id}")
async def update(id: UUID, request: UserUpdate):
    return UserService.edit(id, request)