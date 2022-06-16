from fastapi import APIRouter
from fastapi import Depends,HTTPException,status
from database import SessionLocal,get_db
from models import Student
from schema import Student_response_schema, Student_schema
from hashing import Hash
from routes import JWToken

router = APIRouter(prefix="/student",tags=['Students'])

@router.post("/add")
def add_student(request: Student_schema,db: SessionLocal=Depends(get_db),current_user: Student_schema = Depends(JWToken.get_current_user)):
    stud= Student(name =request.name,email =request.email,password = Hash.hash(request.password),course_opted= request.course_opted)
    db.add(stud)
    db.commit()
    db.refresh(stud)
    return {"Added student":stud}
    
    
@router.get("/get" )
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

