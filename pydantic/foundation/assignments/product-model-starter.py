from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    inStock: bool


input_data = {
    "id": 1,
    "name": "Shoe",
    "price": 100.0,
    "inStock": True,
}

blackHorse = Product(**input_data)

print(blackHorse)
