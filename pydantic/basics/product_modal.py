from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


blackHorse = Product(id=1, name="Black Horse", price=100.0)

lenovoLaptop = Product(id=2, name="Lenovo Laptop", price=1000.0, in_stock=False)

print(blackHorse)

print(lenovoLaptop)
