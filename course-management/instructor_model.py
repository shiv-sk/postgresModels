from sqlmodel import SQLModel, Field, Relationship
from typing import List
from course_model import Course

class Instructor(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    name:str
    email:str = Field(unique=True)
    exp:str
    description:str

    # Relationships
    courses:List[Course] = Relationship(back_populates="instructor")