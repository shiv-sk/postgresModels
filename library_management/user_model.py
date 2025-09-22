from sqlmodel import SQLModel, Field, Relationship
from typing import List
from borrowedbook_model import BorrowedBook

class User(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    name:str
    course:str
    seat_number:str = Field(unique=True)
    dept_id:int = Field(foreign_key="dept.id")

    # Relationships
    borrowed_books:List["BorrowedBook"] = Relationship(back_populates="user")
