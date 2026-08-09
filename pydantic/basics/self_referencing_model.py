from pydantic import BaseModel
from typing import Optional, List


class Comment(BaseModel):
    id: int
    text: str

    replies: Optional[List["Comment"]] = None


Comment.model_rebuild()

comment = Comment(id=1, text="Hello World", replies=[Comment(id=2, text="Reply 1")])

print(comment)
