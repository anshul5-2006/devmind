from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel
from app.core.config import settings
from app.api.routers import health

router = APIRouter()

router.include_router(health.router, prefix="/health", tags=["health"])

@router.get("/")
def root():
    return {"message": "Welcome to DevMind"}

