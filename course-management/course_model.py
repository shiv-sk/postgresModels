from sqlmodel import SQLModel, Field, Relationship
from instructor_model import Instructor
from typing import List
from enrollment_model import Enrollment

class Course(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    title:str
    description:str
    price:str
    cover_image:str
    instructor_id: str = Field(foreign_key="instructor.id")

    # Relationships
    instructor:"Instructor" = Relationship(back_populates="courses")
    enrollments:List["Enrollment"] = Relationship(back_populates="course")