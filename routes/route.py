from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas import MenuItemModel
from database import SessionLocal
import schemas
import crud

router = APIRouter(
    prefix="/menuitem"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[schemas.MenuItemModel])
def get_menu(db: Session = Depends(get_db)):
    menu_items = crud.get_menu(db)
    return menu_items

