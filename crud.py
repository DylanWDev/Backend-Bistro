from sqlalchemy.orm import Session
from models import MenuItem
from schemas import MenuItemModel


def get_menu(db: Session):
    return db.query(MenuItem).all()