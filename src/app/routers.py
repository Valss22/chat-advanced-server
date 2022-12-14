from fastapi import APIRouter
from src.app.user.endpoints import user_router

api_router = APIRouter()
api_router.include_router(user_router)