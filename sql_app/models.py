from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id=Column(Integer, primary_key=True)
    email=Column(String,unique=True,index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)

    items=Relationship("Item",back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id=Column(Integer,primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = Relationship("User",back_populates="items")
