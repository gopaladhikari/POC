from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


input = {
    "id": 1,
    "name": "Gopal Adhikari",
    "is_active": True,
}

user = User(**input)
print(user)
