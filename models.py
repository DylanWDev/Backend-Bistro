from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from database import Base


class Category(Base):
    __tablename__ = "category"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, default="Name")

    # Relationship with MenuItem
    menuitems = relationship("MenuItem", back_populates="category")


class Cuisine(Base):
    __tablename__ = "cuisine"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, default="Name")

    # Relationship with MenuItem
    menuitems = relationship("MenuItem", back_populates="cuisine")


class MenuItem(Base):
    __tablename__ = "menuitems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, default="Name")
    description = Column(Text, default="Description")
    price = Column(Float, default=0.0)
    spicy_level = Column(Integer, default=0)

    category_id = Column(Integer, ForeignKey("category.id"))
    cuisine_id = Column(Integer, ForeignKey("cuisine.id"))

    category = relationship("Category", back_populates="menuitems")
    cuisine = relationship("Cuisine", back_populates="menuitems")