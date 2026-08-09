from pydantic import BaseModel, field_validator, model_validator


class Person(BaseModel):
    fist_name: str
    last_name: str
    age: int

    @field_validator("first_name", "last_name")
    def check_name_and_age(cls, v):
        if not v.istitle():
            raise ValueError("Name must be title case")
        return v


class User(BaseModel):
    username: str
    password: str

    @field_validator("username")
    def normalize_username(cls, v):
        return v.lower().strip()


class Product(BaseModel):
    name: str
    price: float

    @field_validator("price")
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace("$", "").replace(",", ""))
        return v


class DateRange(BaseModel):
    start_date: str
    end_date: str

    @model_validator(mode="after")
    def validate_range(cls, values):
        if values["start_date"] > values["end_date"]:
            raise ValueError("Start date must be before end date")
        return values
