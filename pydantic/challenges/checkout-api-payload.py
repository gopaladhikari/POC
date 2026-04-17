from pydantic import BaseModel, Field, computed_field, model_validator
import uuid
from typing import List, Literal
from datetime import datetime


class Item(BaseModel):
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(default=1, gt=0)


class User(BaseModel):
    email: str
    newsletter_opt_in: bool = False


class Order(BaseModel):
    order_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    customer: User
    cart: List[Item]
    shipping_method: Literal["standard", "express", "overnight"]
    order_date: datetime = Field(default_factory=datetime.now)

    @computed_field
    @property
    def subtotal(self):
        return sum(item.price * item.quantity for item in self.cart)

    @model_validator(mode="after")
    def shipping_method_validate(self):
        if self.shipping_method == "overnight":
            has_premium_item = any(item.price > 50 for item in self.cart)
            if not has_premium_item:
                raise ValueError(
                    "Overnight shipping is only available for premium orders over $50"
                )
        return self
