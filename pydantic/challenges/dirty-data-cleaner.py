from pydantic import BaseModel, field_validator
from typing import List


class BlogPost(BaseModel):
    title: str
    tags: list[str]

    @field_validator("tags", mode="before")
    def check_tags(cls, v):
        new_list = v.split(",")
        trimmed_list = [tag.strip() for tag in new_list]
        return trimmed_list
