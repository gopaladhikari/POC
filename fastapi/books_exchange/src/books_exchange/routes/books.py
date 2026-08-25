from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select, col
from books_exchange.database import get_session
from books_exchange.auth import verify_api_key
from books_exchange.models.books import Books, ReadBook, CreateBook, UpdateBook
from typing import Optional

book_router = APIRouter(prefix="/books", tags=["books"])


@book_router.post("/", response_model=ReadBook, status_code=status.HTTP_201_CREATED)
def create_book(
    book: CreateBook,
    session: Session = Depends(get_session),
    _: str = Depends(verify_api_key),
):
    new_book = Books.model_validate(book)

    session.add(new_book)

    session.commit()

    session.refresh(new_book)

    return new_book


@book_router.get("/", response_model=list[ReadBook])
def get_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    session: Session = Depends(get_session),
    _: str = Depends(verify_api_key),
):
    books_query = select(Books).where(Books.is_sold == False)

    if title:
        books_query = books_query.where(col(Books.title).contains(title))

    if author:
        books_query = books_query.where(col(Books.author).contains(author))

    books = session.exec(books_query).all()

    return books


@book_router.get("/{book_id}", response_model=ReadBook)
def get_book(
    book_id: int,
    session: Session = Depends(get_session),
    _: str = Depends(verify_api_key),
):
    book_query = select(Books).where(Books.id == book_id)

    book = session.exec(book_query).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return book


@book_router.patch("/{book_id}", response_model=ReadBook)
def update_book(
    book_id: int,
    book_data: UpdateBook,
    session: Session = Depends(get_session),
    _: str = Depends(verify_api_key),
):
    book = session.get(Books, book_id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    incoming_update = book_data.model_dump(exclude_unset=True)

    for field, value in incoming_update.items():
        setattr(book, field, value)

    session.commit()

    session.refresh(book)

    return book
