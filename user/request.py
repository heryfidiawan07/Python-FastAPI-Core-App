from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str | None = None
    username: str | None = None
    email: str | None = None
    password: str | None = None
    role_id: str | None = None

class UserUpdate(BaseModel):
    name: str | None = None
    username: str | None = None
    email: str | None = None
    role_id: str | None = None