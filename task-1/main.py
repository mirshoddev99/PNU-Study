from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

my_app = FastAPI()


@my_app.get('/')
def read():
    return {"Hello": "World"}


@my_app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


class Item(BaseModel):
    customer: str
    item_name: str
    item_price: float
    is_offer: Union[bool, None] = None


@my_app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {
        "customer": item.customer,
        "item_id": item_id,
        "item_name": item.item_name,
        "item_price": item.item_price,
        "is_offer": item.is_offer,
    }
