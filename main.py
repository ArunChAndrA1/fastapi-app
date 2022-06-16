from fastapi import Depends, FastAPI
from database import Base,engine
from routes import course,students,login
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methode=["*"],
    allow_headers=["*"]
    
)

Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(course.router)
app.include_router(students.router)


        
        
    
