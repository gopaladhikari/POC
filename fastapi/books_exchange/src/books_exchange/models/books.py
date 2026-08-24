from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Books(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    author: str = Field(index=True)
    price: int
    is_sold: bool = False

    # Foregin Key
    user_id: int = Field(foreign_key="users.id")
    owner: Optional["Users"] = Relationship(back_populates="books")


# Validation


class CreateBook(SQLModel):
    title: str
    author: str
    price: int


class ReadBook(SQLModel):
    id: int
    title: str
    author: str
    price: int
    is_sold: bool


# Circular import handling

from .users import Users

Users.model_rebuild()
