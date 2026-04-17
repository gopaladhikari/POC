from pydantic import BaseModel
from typing import Literal


class Task(BaseModel):
    title: str
    status: Literal["todo", "in_progress", "done"]
