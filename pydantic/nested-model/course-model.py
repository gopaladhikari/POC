from pydantic import BaseModel
from typing import List


class Course(BaseModel):
    id: int
    name: str
    modules: List[Module]


class Module(BaseModel):
    id: int
    name: List[str]
    lessons: List[Lesson]


class Lesson(BaseModel):
    id: int
    topic: str


# Course.model_rebuild() No need to do this because it is not referenced itseld
# Module.model_rebuild() No need to do this because it is not referenced itseld
