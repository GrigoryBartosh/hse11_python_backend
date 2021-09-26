from fastapi import APIRouter, HTTPException

from src.common import Item
from src import model


router = APIRouter()


@router.get("/")
async def root_endpoint():
    return model.get_hello_message()


@router.get("/api/{id}")
async def read_item_info_endpoint(id: int):
    try:
        return model.read_item_info(id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/items/")
async def create_item_endpoint(item: Item):
    try:
        return model.create_item(item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))