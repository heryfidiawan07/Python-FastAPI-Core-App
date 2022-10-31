from fastapi import APIRouter
from user.model import UserModel
from user.service import UserService
from user.request import UserCreate, UserUpdate

router = APIRouter()

@router.get("/user")
async def index():
    return UserService.all()

@router.get("/user/{id}")
async def show(id: str):
    return UserService.find(id)

@router.delete("/user/{id}")
async def delete(id: str):
    UserService.destroy(id)
    return "Data was deleted"

@router.post("/user")
async def store(request: UserCreate):
    return UserService.create(request)

@router.put("/user/{id}")
async def update(id: str, request: UserUpdate):
    return UserService.edit(id, request)