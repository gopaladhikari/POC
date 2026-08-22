from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import create_tables
from .models import Reviews
from .routes.reviews import reviews_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Tables created")
    yield


app = FastAPI(
    title="Rangmanch API",
    description="A theartical api for handling reviews of the movies.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(reviews_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
