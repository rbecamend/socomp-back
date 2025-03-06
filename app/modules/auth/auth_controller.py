from fastapi import APIRouter, HTTPException
from app.modules.auth.auth_schemas import LoginRequest, RegisterRequest
from app.modules.auth.auth_service import login_service, register_service

router = APIRouter()

@router.post("/login")
async def login(login_data: LoginRequest):
    pass

@router.post("/register")
async def register(register_data: RegisterRequest):
    pass