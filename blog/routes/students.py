from typing import List
from fastapi import APIRouter
from fastapi import Depends,HTTPException,status
from blog.database import SessionLocal,get_db
from blog.models import Student
from blog.schema import Student_response_schema, Student_schema
from blog.hashing import Hash
from blog import JWToken

router = APIRouter(prefix="/student",tags=['Students'])

@router.post("/add")
def add_student(request: Student_schema,db: SessionLocal=Depends(get_db),current_user: Student_schema = Depends(JWToken.get_current_user)):
    stud= Student(name =request.name,email =request.email,password = Hash.hash(request.password),course_1= request.course_1,course_2= request.course_2)
    db.add(stud)
    db.commit()
    db.refresh(stud)
    return {"Added student":stud}
    
    
@router.get("/get",response_model=List[Student_response_schema])
def all_students(db:SessionLocal=Depends(get_db),current_user: Student_schema = Depends(JWToken.get_current_user)):
    studs=db.query(Student).all()
    if not studs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No students found, Please add student")
    return studs

@router.get("/get/{id}",response_model=Student_response_schema )
def get_student(id,db:SessionLocal=Depends(get_db),current_user: Student_schema = Depends(JWToken.get_current_user)):
    studs=db.query(Student).filter(Student.id==id).first()
    if not studs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No students found, Please add student")
    return studs

