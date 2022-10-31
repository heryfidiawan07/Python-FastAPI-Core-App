from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str | None = None
    permission_id: list | None = None

class RoleUpdate(BaseModel):
    name: str | None = None
    permission_id: list | None = None