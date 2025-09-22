from typing import Optional , List
from sqlmodel import SQLModel, Field, Relationship
from enrollment_model import Enrollment

class Student(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    name:str
    email:str = Field(unique=True)
    college: Optional[str]

    # Relationships
    enrollments:list[Enrollment] = Relationship(back_populates="student")