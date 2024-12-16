from typing import Union
from fastapi import APIRouter
from common.common_domain.entity.test import opsa

user_controller = APIRouter()

@user_controller.get("/")
def read_root():
    opsa()
    return {"Hello": "World"}


@user_controller.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}