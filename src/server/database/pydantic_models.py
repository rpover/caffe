from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class User(BaseModelModify):
    name: str


class AuthData(BaseModelModify):
    login: str
    password: Optional[str]
    user_id: int


class Staff(BaseModelModify):
    name: str


class FiredStaff(BaseModelModify):
    staff_id: int


class Menu(BaseModelModify):
    name: str
    price: float
    cooking_time: float


class Orders(BaseModelModify):
    user_id: int
    menu_postion_id: int


class UserAddress(BaseModelModify):
    address: str
    user_id: int


class ProductOrderds(BaseModelModify):
    product_id: int
    count: int


class Product(BaseModelModify):
    name: str
    count: int

