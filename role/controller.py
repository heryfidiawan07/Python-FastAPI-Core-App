from fastapi import APIRouter
from role.model import RoleModel
from role.service import RoleService
from role.request import RoleCreate, RoleUpdate
from uuid import UUID

router = APIRouter()

@router.get("/role")
async def index():
    return RoleService.all()

@router.get("/role/{id}")
async def show(id: UUID):
    return RoleService.find(id)

@router.delete("/role/{id}")
async def delete(id: UUID):
    RoleService.destroy(id)
    return "Data was deleted"

@router.post("/role")
async def store(request: RoleCreate):
    return RoleService.create(request)

@router.put("/role/{id}")
async def update(id: UUID, request: RoleUpdate):
    return RoleService.edit(id, request)