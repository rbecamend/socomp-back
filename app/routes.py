from fastapi import APIRouter
from app.modules.auth.auth_controller import router as login, register

router = APIRouter()

router.include_router(login)
router.include_router(register)