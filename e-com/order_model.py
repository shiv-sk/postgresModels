from sqlmodel import SQLModel, Field, Relationship
from user_model import User
from product_model import Product
from typing import List

class Order(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    user_id:int = Field(foreign_key="user.id")

    # Relationships
    user:User = Relationship(back_populates="orders")
    products:List[Product] = Relationship(back_populates="orders" , link_model="OrderProduct")