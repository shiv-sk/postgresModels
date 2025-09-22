from sqlmodel import SQLModel, Field, Relationship
from typing import List
from order_model import Order


class Product(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    name:str
    category:str = Field(index=True)
    brand:str = Field(index=True)

    # Relationship
    orders:List[Order] = Relationship(back_populates="products" , link_model="OrderProduct")