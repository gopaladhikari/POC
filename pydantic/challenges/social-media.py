from pydantic import BaseModel, field_validator, Field
from typing import List


class Post(BaseModel):
    username: str = Field(..., min_length=4, max_length=20)
    likes: int = Field(default=0, ge=0)
    tags: list[str]

    @field_validator("tags")
    def check_tags(cls, v):
        new_tags_list = [tag.lower() for tag in v]
        return new_tags_list
