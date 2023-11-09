from typing import Optional

from pydantic import BaseModel


class CategoryModel(BaseModel):
    id: int
    name: str | None

class CuisineModel(BaseModel):
    id: int
    name: str | None

class MenuItemModel(BaseModel):
    id: int
    title: str | None
    description: str | None
    price: float | None
    spicy_level: int
    category_id: int
    cuisine_id: int

    class Config:
        orm_mode = True
    