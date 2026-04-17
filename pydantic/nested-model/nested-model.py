from pydantic import BaseModel
from typing import List, Optional


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


class Comment(BaseModel):
    id: int
    text: str
    replies: Optional[List["Comment"]] = None  # self referential


Comment.model_rebuild()  # this is because it is referecing itself


address = Address(street="123 Main St", city="Anytown", postal_code="12345")

user = User(id=1, name="John Doe", address=address)

comment = Comment(id=1, text="Hello World", replies=[Comment(id=2, text="Reply 1")])

print(user)
print(comment)
print(address)
