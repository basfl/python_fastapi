from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
   this is for reference in case of 
   connecting using psycopg2
"""

while True:
    try:
        conn = psycopg2.connect(host=settings.database_hostname, database=settings.database_name,
                                user=settings.database_username, password=settings.database_password, cursor_factory=RealDictCursor)
        curser = conn.cursor()
        print("DB connection was successful ")
        break
    except Exception as error:
        print("connection to DB failed")
        print(error)
        time.sleep(3)
