from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    address: Address
    tags: List[str] = []
    created_at: datetime

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")}
    )


user = User(
    id=1,
    name="John Doe",
    email="q2H8o@example.com",
    tags=["tag1", "tag2"],
    address=Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip="12345",
    ),
    created_at=datetime.now(),
)

python_dict = user.model_dump()


print(python_dict)

print("=" * 90)

json_string = user.model_dump_json()
print(json_string)
