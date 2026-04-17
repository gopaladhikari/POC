from pydantic import BaseModel, model_validator, field_validator, computed_field


class User(BaseModel):
    id: int
    username: str

    @field_validator("username")
    def check_username(cls, v):
        if len(v) < 5:
            raise ValueError("Username must be at least 5 characters long")
        return v


class Signup(BaseModel):
    username: str
    password: str
    confirmPassword: str
    email: str

    @model_validator(mode="after")
    def matchPassword(cls, values):
        if values["password"] != values["confirmPassword"]:
            raise ValueError("Passwords do not match")
        return values


class Product(BaseModel):
    id: int
    price: float
    quantity: int

    @computed_field
    @property
    def total(self):
        return self.price * self.quantity
