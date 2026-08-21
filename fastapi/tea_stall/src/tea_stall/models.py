from pydantic import BaseModel


class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    category: str
    price: float
    is_available: bool


class MenuResponse(BaseModel):
    status: str = "success"
    count: int
    items: list[MenuItem]
