from enum import Enum
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, func


class OrderStatus(str, Enum):
    PREPARING = "preparing"
    PICKED_UP = "picked_up"
    IN_TRANSIT = "in_transit"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_name: str
    delivery_address: str
    items: str
    status: OrderStatus = Field(default=OrderStatus.PREPARING)
    created_at: datetime = Field(sa_column_kwargs={"server_default": func.now()})
    updated_at: datetime = Field(
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()}
    )


# Validation classes


class OrderCreate(SQLModel):
    customer_name: str
    delivery_address: str
    items: str


class OrderUpdate(SQLModel):
    status: OrderStatus


class StatusLog(SQLModel):
    order_id: int
    status: OrderStatus
    created_at: datetime
