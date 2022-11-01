from pydantic import BaseModel
from uuid import UUID

class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    password: str
    role_id: UUID

class UserUpdate(BaseModel):
    name: str
    username: str
    email: str
    role_id: UUID