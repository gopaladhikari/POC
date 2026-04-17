from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        max_length=30,
        min_length=3,
        description="Name of an employee",
        examples=["Gopal Adhikari"],
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000,
        description="Salary of an employee",
        examples=[1000, 10000],
    )
