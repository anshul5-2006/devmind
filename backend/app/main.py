from fastapi import FastAPI
from pydantic import BaseModel
from app.core.config import settings
from .api import router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")
   


app = FastAPI(title= settings.app_name, version= settings.app_version, description="DevMind API", lifespan=lifespan)
app.include_router(router.router, prefix="/api", tags=["api"])

class Item(BaseModel):
    name: str
    price: float
    on_offer: bool = None



@app.get("/")
def root():
    return {"message": "Welcome to DevMind"}

@app.get("/{item_id}")
def read_item_id(item_id: int):
    return {"item_id": item_id}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    
    return {"item_id": item_id, "q": q}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item.name, "price": item.price, "on_offer": item.on_offer}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id, "status": "deleted"}
