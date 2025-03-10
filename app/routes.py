from fastapi import APIRouter
from app.modules.auth.auth_controller import router as auth_router

router = APIRouter()

router.include_router(auth_router)