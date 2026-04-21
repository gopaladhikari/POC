from fastapi import FastAPI, Depends
from database import session
import database_model
from models import Product
from sqlalchemy.orm import Session

from database import engine

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/products")
def read_products(db: Session = Depends(get_db)):
    products = db.query(database_model.Product).all()
    return products


@app.get("/products/{id}")
def read_product(id: int, db: Session = Depends(get_db)):
    product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )
    if product is None:
        return {"message": "Product not found"}
    return {"message": "product found", "product": product}


@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = database_model.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    return {"message": "Product created"}


@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    current_product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )

    if current_product is None:
        return {"message": "Product not found"}

    update_data = product.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(current_product, key, value)

    db.commit()

    db.refresh(current_product)
    return {"message": "Product updated"}


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )

    if product is None:
        return {"message": "Product not found"}

    db.delete(product)

    db.commit()

    return {"message": "Product deleted"}
