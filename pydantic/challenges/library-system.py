from pydantic import BaseModel, Field, computed_field
from typing import List


class Book(BaseModel):
    title: str
    author: str
    page: int = Field(..., gt=0)


class Library(BaseModel):
    name: str
    books: List[Book]

    @computed_field
    @property
    def totalBooks(self) -> int:
        return len(self.books)
