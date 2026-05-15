from datetime import datetime, timezone, timedelta
from typing import Annotated
from uuid import UUID, uuid4
from fastapi import Depends
from passlib.context import CryptContext
import jwt
from sqlalchemy.orm import Session
from models.users import User
from schemas.users import User as PydanticUser
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from dotenv import load_dotenv
import os
import logging

load_dotenv()

algorithm = os.getenv("HS256")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
access_token_expiry = os.getenv("ACCESS_TOKEN_EXPIRY")


oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password: str, hashed_password: str):
    return bcrypt_context.verify(password, hashed_password)


def get_password_hash(password: str):
    return bcrypt_context.hash(password)


def create_access_token(email: str, user_id: UUID, expires: timedelta):

    if not algorithm or not access_token_secret:
        raise EnvironmentError("JWT environment variables are missing")

    encode = {
        "sub": email,
        "id": str(user_id),
        "exp": datetime.now(timezone.utc) + expires,
    }

    return jwt.encode(encode, access_token_secret, algorithm=algorithm)


def login_useer(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()

    if not user or not isinstance(user.password, str):
        logging.warning(f"Authentication failed for {email}")
        return None

    if not verify_password(password, user.password):
        logging.warning(f"Invalid password for {email}")
        return None

    return user


def get_user(user_id: UUID, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def change_password(user_id: UUID, password: str, db: Session):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            logging.warning(f"User {user_id} not found")
            return None
        hashed_password = get_password_hash(password)
        user.password = hashed_password
        db.commit()
        return user
    except Exception as e:
        logging.warning(f"Error changing password for {user_id}: {e}")
