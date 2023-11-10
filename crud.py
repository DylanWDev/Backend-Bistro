from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from models import MenuItem, Category, Cuisine
from schemas import MenuItemModel

def get_menu(db: Session):
    return db.query(MenuItem, Category.name.label('category_name'), Cuisine.name.label('cuisine_name')) \
        .join(Category, MenuItem.category_id == Category.id) \
        .join(Cuisine, MenuItem.cuisine_id == Cuisine.id) \
        .all()
