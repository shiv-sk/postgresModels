from sqlmodel import SQLModel, Field, Relationship
from event_model import Event

class Review(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    event_id:int = Field(foreign_key="event.id")
    rating:float
    content:str

    # Relationships
    event:"Event" = Relationship(back_populates="reviews")