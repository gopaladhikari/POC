from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()


class User(BaseModel):
    email: EmailStr
    username: str
    password: str
    full_name: str


class Settings(BaseModel):
    app_name: str = "FastAPI"
    theme: str
    language: str


def get_settings():
    return Settings(theme="dark", language="en")


@app.post("/register")
def register(user: User):
    return {"message": f"Welcome {user.username}!"}


@app.get("/settings")
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings
