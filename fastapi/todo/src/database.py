from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()


db_url = os.getenv("DB_URL")

if not db_url:
    raise EnvironmentError("database url not found")

Base = declarative_base()


engine = create_engine(db_url)

session = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


DbSession = Annotated[session, Depends(get_db)]
