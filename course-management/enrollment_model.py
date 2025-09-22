from sqlmodel import SQLModel, Field, Relationship
from student_model import Student
from course_model import Course

class Enrollment(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    student_id:Student = Field(foreign_key="student.id")
    course_id:Course = Field(foreign_key="course.id")

    # Relationships
    student:"Student" = Relationship(back_populates="enrollments")
    course:"Course" = Relationship(back_populates="enrollments")