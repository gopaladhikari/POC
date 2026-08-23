from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import create_tables
from .models import Orders
from .orders.routes import orders_router
from .stats.routes import stats_router


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


app.include_router(orders_router)
app.include_router(stats_router)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
