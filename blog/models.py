from blog.database import Base
from sqlalchemy import ARRAY, Column, Float, ForeignKey,Integer,String
from sqlalchemy.orm import relationship,relationships



class Course(Base):
    __tablename__="courses"
    course_id= Column(Integer,primary_key=True)
    course_name = Column(String,nullable=False)
    duration_in_hours = Column(Float,nullable=False)
    # student = relationship("Student",back_populates="opted_courses")
    
class Student(Base):
    __tablename__="students"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password= Column(String,nullable=False)
    course_1 = Column(Integer,ForeignKey('courses.course_id'))
    course_2 = Column(Integer,ForeignKey('courses.course_id'))
    opted_course_1=relationship("Course",foreign_keys=[course_1])
    opted_course_2=relationship("Course",foreign_keys=[course_2])
    
    