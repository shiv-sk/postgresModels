from sqlmodel import SQLModel, Field, Relationship
from typing import List
from order_model import Order


class User(SQLModel , table=True):
    id:int = Field(default=None , nullable=False , primary_key=True)
    name:str
    email:str = Field(unique=True)
    password:str
    mobile:str
    address:str
    pincode:str

    # Relationship
    orders:List[Order] = Relationship(back_populates="user")