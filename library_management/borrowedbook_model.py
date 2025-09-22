from sqlmodel import SQLModel, Field, Relationship
from user_model import User
from book_model import Book
import datetime

class BorrowedBook(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    user_id:int = Field(foreign_key="user.id")
    book_id:int  = Field(foreign_key="book.id")
    borrowed_date:datetime.date
    return_date:datetime.date

    # Relationships
    user:"User" = Relationship(back_populates="borrowed_books")
    book: "Book" = Relationship(back_populates="borrowed_books")