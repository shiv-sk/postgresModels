from sqlmodel import SQLModel, Field, Relationship
import datetime
from typing import List
from borrowedbook_model import BorrowedBook
class Book(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    name:str
    author:str
    publication:str
    published_year:datetime.date

    # Relationships
    borrowed_books: List["BorrowedBook"] = Relationship(back_populates="book")