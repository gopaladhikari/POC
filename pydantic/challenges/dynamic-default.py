from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    username: str
    created_at: datetime = Field(default_factory=datetime.now)
