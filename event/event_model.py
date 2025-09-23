from sqlmodel import SQLModel, Field, Relationship
import datetime
from typing import List
from review_model import Review

class Event(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    event_type:str
    name:str = Field(unique=True)
    length:str
    production:str
    released_year:datetime.date
    budget:float

    # Relationships
    reviews:List["Review"] = Relationship(back_populates="event")