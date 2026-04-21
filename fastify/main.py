from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()


class BaseProduct(BaseModel):
    name: str
    price: float
    quantity: int
    description: str


class Product(BaseProduct):
    id: int


products: List[Product] = [
    Product(id=1, name="Apple", price=0.5, quantity=10, description="A fruit"),
    Product(id=2, name="Orange", price=0.7, quantity=5, description="A citrus fruit"),
    Product(id=3, name="Banana", price=0.2, quantity=7, description="A berry"),
    Product(id=4, name="Papaya", price=1, quantity=12, description="A tropical fruit"),
]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/products")
def read_products():
    return {"products": products}


@app.get("/products/{id}")
def read_product(id: int):
    for product in products:
        if product.id == id:
            return {"product": product}
    return {"message": "Product not found"}


@app.post("/products")
def create_product(product: BaseProduct):
    id = len(products) + 1
    products.append(Product(id=id, **product.model_dump()))
    return {"message": "Product created", "products": products}


@app.put("/products/{id}")
def update_product(id: int, product: BaseProduct):
    for i, p in enumerate(products):
        if p.id == id:
            products[i] = Product(id=id, **product.model_dump())
            return {"message": "Product updated", "products": products}
    return {"message": "Product not found"}


@app.delete("/products/{id}")
def delete_product(id: int):
    for i, p in enumerate(products):
        if p.id == id:
            products.pop(i)
            return {"message": "Product deleted", "products": products}
    return {"message": "Product not found"}
