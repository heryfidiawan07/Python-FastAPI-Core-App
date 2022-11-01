from pydantic import BaseModel
from uuid import UUID

class RoleCreate(BaseModel):
    name: str
    permission_id: list[UUID]

class RoleUpdate(BaseModel):
    name: str
    permission_id: list[UUID]