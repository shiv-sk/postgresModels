from sqlmodel import SQLModel , Field

class Dept(SQLModel , table=True):
    id:int = Field(default=None , primary_key=True)
    name:str = Field(unique=True)
