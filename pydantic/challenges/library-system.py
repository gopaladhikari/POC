from pydantic import BaseModel, List, Field, computed_field


class Book(BaseModel):
    title: str
    author: str
    page: int = Field(..., gt=0)


class Library(BaseModel):
    name: str
    books: List[Book]

    @computed_field
    @property
    def totalBooks(self):
        return len(self.books)
