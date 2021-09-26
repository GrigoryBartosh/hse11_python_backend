from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    username: Optional[str] = None
    price: float
    item_name: str


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/api/{id}")
async def read_item(id: int, q: Optional[str] = None):
    return {"id": id, "q": q}


@app.post("/items/")
async def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="The price cannot be negative")

    response = Item(
        username=item.username,
        price=0.8 * item.price,
        item_name=f"{item.item_name} скидка"
    )
    return response