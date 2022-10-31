from fastapi import FastAPI
from user.module import userRouter
from role.module import roleRouter
from config.database import Base, engine
from permission.model import PermissionModel, MenuModel, RolePermissionModel

app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/")
async def healthy():
    return {"app": "RESTful API Core App"}

app.include_router(userRouter)
app.include_router(roleRouter)
