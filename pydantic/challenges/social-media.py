from pydantic import BaseModel, field_validator
from typing import List


class Post(BaseModel):
    username: str
    likes: int = 0
    tags: list[str]

    @field_validator("tags")
    def check_tags(cls, v):
        new_tags_list: List[str] = []
        for tag in v:
            new_tags_list.append(tag.lower())
        return new_tags_list

    @field_validator("likes")
    def check_likes(cls, v):
        if v < 0:
            raise ValueError("Likes cannot be negative")
        return v
