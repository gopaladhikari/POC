from pydantic import BaseModel, field_validator, model_validator


class Item(BaseModel):
    name: str
    price: float

    @field_validator("price")
    def check_price(cls, v):
        if v < 0:
            raise ValueError("Price cannot be negative")
        return v


class Register(BaseModel):
    username: str
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_passwords_match(cls, values):
        if values["password"] != values["confirm_password"]:
            raise ValueError("Passwords do not match")
        return values
