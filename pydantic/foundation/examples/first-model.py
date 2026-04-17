from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    isActive: bool


input_data = {
    "id": 1,
    "name": "Gopal Adhikari",
    "email": "gopal@example.com",
    "isActive": True,
}

input_data2 = {
    "id": 2,
    "name": "Gopal Adhikari",
    "email": "gopal@example.com",
    "isActive": "True",
}


gopal = User(**input_data)
adhikari = User(**input_data2)
print(gopal)
print(adhikari)
