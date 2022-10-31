from fastapi import APIRouter
from role.model import RoleModel
from role.service import RoleService
from role.request import RoleCreate, RoleUpdate

router = APIRouter()

@router.get("/role")
async def index():
    return RoleService.all()

@router.get("/role/{id}")
async def show(id: str):
    return RoleService.find(id)

@router.delete("/role/{id}")
async def delete(id: str):
    RoleService.destroy(id)
    return "Data was deleted"

@router.post("/role")
async def store(request: RoleCreate):
    return RoleService.create(request)

@router.put("/role/{id}")
async def update(id: str, request: RoleUpdate):
    return RoleService.edit(id, request)