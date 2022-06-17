from fastapi import APIRouter
from fastapi import Depends,HTTPException,status
from blog.database import Base, SessionLocal,get_db
from blog.models import Course
from blog.schema import Course_schema
from blog import JWToken




router = APIRouter(
    prefix="/course",
    tags=['Course']
)

@router.post("/add")
def add_course(request: Course_schema,db: SessionLocal =Depends(get_db),current_user: Course_schema = Depends(JWToken.get_current_user)):
    course = Course(course_name=request.course_name,duration_in_hours=request.duration_in_hours) 
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

@router.get("/get")
def all_courses(db: SessionLocal =Depends(get_db),current_user: Course_schema = Depends(JWToken.get_current_user)):
    courses= db.query(Course).all()
    if not courses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No courses found, Please add courses")
    return courses

@router.get("/get/{id}" )
def get_course(id,db: SessionLocal =Depends(get_db),current_user: Course_schema = Depends(JWToken.get_current_user)):
    courses= db.query(Course).filter(Course.course_id==id).first()
    if not courses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Course with {id} not found")
    return courses

@router.put("/{id}" )
def edit_course(id,request: Course_schema,db: SessionLocal =Depends(get_db),current_user: Course_schema = Depends(JWToken.get_current_user)):
    course = db.query(Course).filter(Course.course_id==id).update(dict(request),synchronize_session=False)
    course = db.query(Course).filter(Course.course_id==id).first()
    if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Course with {id} not found")
        
    db.commit()
    db.refresh(course)
    return "Updated data:",course

@router.delete("/{id}" )
def del_course(id,db: SessionLocal =Depends(get_db),current_user: Course_schema = Depends(JWToken.get_current_user)):
    course=db.query(Course).filter(Course.course_id==id).delete(synchronize_session=False)
    if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Course with {id} not found")
        
    db.commit()
    return "Deleted course"
