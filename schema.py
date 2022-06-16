from pydantic import BaseModel
from typing import Union

class Student_schema(BaseModel):
    name: str
    email:str
    password: str
    course_opted: int
    # course_2: int
    class Config:
        orm_mode=True


class Course_schema(BaseModel):
    course_name: str
    duration_in_hours: float
    
    class Config:
        orm_mode=True       
        
class Student_response_schema(BaseModel):
    name: str
    email:str
    course: Course_schema
    # course: Course_schema
    class Config:
        orm_mode=True 
        
        
class login(BaseModel):
    email:str
    password:str
    class Config:
        orm_mode=True
        
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None

