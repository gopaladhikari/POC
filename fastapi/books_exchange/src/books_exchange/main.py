from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import create_table
from .models.books import Books
from .models.users import Users
from .routes.books import book_router
from .routes.users import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    yield


app = FastAPI(
    title="Books Exchange API",
    description="An API for exchanging books between users.",
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(book_router)
app.include_router(user_router)
