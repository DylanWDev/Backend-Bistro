from typing import List
from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from database import Base


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")

    # def __repr__(self) -> str:
    #     return f"Category(id={self.id!r}, name={self.name!r})"
    

class Cuisine(Base):
    __tablename__ = "cuisine"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")

    # def __repr__(self) -> str:
    #     return f"Cuisine(id={self.id!r}, name={self.name!r})"
    

class MenuItem(Base):
    __tablename__ = "menuitems"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String, default="Name")
    description: Mapped[str] = Column(String, default="Description")
    price: Mapped[float] = Column(Integer, default="Price")
    spicy_level: Mapped[int] = Column(Integer, default="Spicy Level")

    category_id: Mapped[int] = Column(Integer, ForeignKey("category.id"))
    cuisine_id: Mapped[int] = Column(Integer, ForeignKey("cuisine.id"))

    category = relationship("Category", back_populates="menuitems")
    cuisine = relationship("Cuisine", back_populates="menuitems")

    def __repr__(self) -> str:
        return f"MenuItem(id={self.id!r}, title={self.title!r}, description={self.description!r}, price={self.price!r}, spicy_level={self.spicy_level}, category_id={self.category_id!r}, cuisine_id={self.cuisine_id!r}, category={self.category!r}, cuisine={self.cuisine!r})"

    
