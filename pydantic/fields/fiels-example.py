from pydantic import BaseModel
from typing import Optional, List, Dict


class Cart(BaseModel):
    id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    author: str
    imageUrl: Optional[str]
