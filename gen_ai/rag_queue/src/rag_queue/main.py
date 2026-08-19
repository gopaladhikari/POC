from fastapi import FastAPI
from contextlib import asynccontextmanager
from .queues.worker import process_query
from .clients.rq_client import queue
from .qdrant import initialize_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Initializing Application Lifespan...")

    app.state.vector_store = initialize_database()

    print("✅ Vector database is ready! Server is starting.")

    yield

    print("👋 Closing Application Lifespan...")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/chat")
def chat(query: str):
    job = queue.enqueue(process_query, query)

    return {"status": job.get_status(), "job_id": job.id}


@app.get("/result/{job_id}")
def get_result(job_id: str):

    job = queue.fetch_job(job_id)

    if not job:
        return {"status": "not found", "result": None}

    print(job.return_value())

    result = job.return_value()

    return {
        "status": job.get_status(),
        "result": result,
    }
