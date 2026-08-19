from fastapi import APIRouter

router = APIRouter()

@router.get("/{health}")
def get_health(health: str):
    return {"status": "ok", "health": health}