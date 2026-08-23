from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import create_tables
from .models import Orders


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="Delivery API",
    description="API for managing deliveries and orders",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
