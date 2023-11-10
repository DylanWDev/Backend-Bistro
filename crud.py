from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from models import MenuItem, Category, Cuisine
from schemas import MenuItemModel

def get_menu(db: Session):
    return db.query(MenuItem, Category.name.label('category_name'), Cuisine.name.label('cuisine_name')) \
        .join(Category, MenuItem.category_id == Category.id) \
        .join(Cuisine, MenuItem.cuisine_id == Cuisine.id) \
        .all()

# def get_dish(db: Session, item_id: int):
#     menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()

#     if menu_item is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dish Not Found")
    

#     menu_item_model = MenuItemModel(
#             "id": item.id,
#             "title": item.title,
#             "description": item.description,
#             "price": item.price,
#             "spicy_level": item.spicy_level,
#             "category": category_name,
#             "cuisine": cuisine_name
#     )

#     return menu_item_model
