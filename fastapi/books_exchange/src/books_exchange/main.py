from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import create_table
from .models.books import Books
from .models.users import Users


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
