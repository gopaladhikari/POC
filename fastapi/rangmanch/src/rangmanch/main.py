from fastapi import FastAPI

app = FastAPI(
    title="Rangmanch",
    description="A theartical api for handling reviews of the movies.",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
