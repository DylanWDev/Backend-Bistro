from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
import crud
from schemas import MenuItemModel, CategoryModel, CuisineModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[MenuItemModel])
async def get_menu_items(db: Session = Depends(get_db)):
    menu_items = crud.get_menu(db)
    return menu_items
