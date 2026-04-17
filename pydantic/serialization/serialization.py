from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str


class Person(BaseModel):
    name: str
    age: int
    address: Address
    created_at: datetime

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )


address = Address(street="123 Main St", city="San Francisco", state="CA", zip="94105")

gopal = Person(
    name="Gopal",
    age=30,
    created_at=datetime.now(),
    address=address,
)


# Using model_dump -> Dict

print(gopal.model_dump())

# Using json_dumps -> JSON

print(gopal.model_dump_json())
