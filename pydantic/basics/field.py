from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    author: str
    image_url: Optional[str] = None


cart_1 = Cart(id=1, items=["item1", "item2"], quantities={"item1": 1, "item2": 2})
blog_1 = BlogPost(id=1, title="title", content="content", author="author")

print(cart_1)
print(blog_1)
