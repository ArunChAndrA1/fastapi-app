from fastapi import APIRouter
from routes.JWToken import create_access_token

from fastapi.security import OAuth2PasswordRequestForm
from database import SessionLocal,get_db
from models import Student
from fastapi import Depends,status,HTTPException
from hashing import Hash

router=APIRouter(tags=['Authentication'])

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(),db:SessionLocal=Depends(get_db)):
    admin='admin_arun@effigo.in'
    if request.username==admin and request.password=='admin':
        access_token = create_access_token(data={"sub": admin})
        return {"access_token": access_token, "token_type": "bearer"}
        
        
    user=db.query(Student).filter(Student.email==request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid credentials")
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid password")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}