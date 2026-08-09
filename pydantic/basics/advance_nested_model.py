from pydantic import BaseModel
from typing import List, Optional, Union


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str


class Company(BaseModel):
    name: str

    address: Optional[Address] = None


class Employee(BaseModel):
    name: str
    age: int
    company: Optional[Company] = None


class TextContent(BaseModel):
    text: str
    content: str


class ImageContent(BaseModel):
    type: str
    url: str
    alt_text: str


class Article(BaseModel):
    title: str
    content: Union[TextContent, ImageContent]


class Country(BaseModel):
    name: str
    code: str


class State(BaseModel):
    name: str
    country: Country


class City(BaseModel):
    name: str
    state: State


class Organization(BaseModel):
    name: str
    address: Address

    branches: Optional[List[Address]] = None
