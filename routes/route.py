# routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import get_menu 
from models import MenuItem

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all")
async def get_all_menu_items(db: Session = Depends(get_db)):
    menu_items = get_menu(db)
    result = []
    for item, category_name, cuisine_name in menu_items:
        result.append({
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "spicy_level": item.spicy_level,
            "category": category_name,
            "cuisine": cuisine_name
        })
    return result



    


