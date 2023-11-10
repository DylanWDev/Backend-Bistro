from schemas import MenuItemModel
from sqlalchemy.orm import Session, aliased, joinedload
from models import MenuItem, Cuisine, Category

def get_menu_items(db:Session):
    menu_items_query = (
        db.query(MenuItem).all()
    )
    
    return menu_items_query



def get_category_and_cuisine_type(db:Session):
    menu_items_with_category_and_cuisine_query = (
        db.query(MenuItem).options(joinedload(MenuItem.categories)).all()
    )
    
    return menu_items_with_category_and_cuisine_query