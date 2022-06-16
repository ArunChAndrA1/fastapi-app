from database import Base
from sqlalchemy import Column, Float, ForeignKey,Integer,String
from sqlalchemy.orm import relationship,relationships

class Course(Base):
    __tablename__="courses"
    course_id= Column(Integer,primary_key=True)
    course_name = Column(String,nullable=False)
    duration_in_hours = Column(Float,nullable=False)
    student = relationship("Student",back_populates="course")


class Student(Base):
    __tablename__="students"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password= Column(String,nullable=False)
    course_opted = Column(Integer,ForeignKey('courses.course_id'))
    # course_2 = Column(Integer,foreign_keys=['courses.course_id'])
    course = relationship("Course",back_populates="student")
    