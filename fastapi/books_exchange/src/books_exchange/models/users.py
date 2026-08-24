from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    collage: str

    books: list["Books"] = Relationship(back_populates="owner")


# Request Validation Models


class UserCreate(SQLModel):
    username: str
    email: str
    password: str
    collage: str


class ReadUser(SQLModel):
    id: int
    username: str
    email: str
    collage: str


# Circular import handling
from .books import Books

Users.model_rebuild()
