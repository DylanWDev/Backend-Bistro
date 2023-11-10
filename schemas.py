from typing import Optional, List, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


class CategoryModel(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None


class CuisineModel(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None


class MenuItemModel(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    spicy_level: Optional[int] = None
    category_id: Optional[int] = None
    cuisine_id: Optional[int] = None
    