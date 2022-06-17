from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_URL= "sqlite:///./data.db"
engine = create_engine(DB_URL,echo=True,connect_args={'check_same_thread':False})

Base = declarative_base()

SessionLocal=sessionmaker(bind=engine,autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

