from fastapi import APIRouter, Depends, Request, Header
from fastapi.security import OAuth2PasswordBearer
from user.model import UserModel
from auth.service import AuthService
from auth.request import Login, Register

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/login")
async def login(request: Login):
    return AuthService.login(request)

@router.post("/register")
async def regiter(request: Register):
    return AuthService.register(request)

@router.get("/me")
async def me(access_token: str | None = Header(default=None)):
    # return {"access_token": access_token}
    return AuthService.me(access_token)