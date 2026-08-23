from fastapi import APIRouter, Depends, HTTPException, status, Query
from delivery.database import get_session
from delivery.models import Orders, OrderCreate, OrderUpdate, StatusLog, OrderStatus
from sqlmodel import Session, select
from typing import Optional
from datetime import datetime, date

orders_router = APIRouter(prefix="/orders", tags=["Orders"])


@orders_router.get(
    "/",
    response_model=list[Orders],
    status_code=status.HTTP_200_OK,
    description="Get all orders",
)
def get_orders(
    order_status: Optional[OrderStatus] = Query(
        default=None, description="Filter orders by status"
    ),
    created_date: Optional[date] = Query(
        default=None, description="Filter orders by created date (YYYY-MM-DD)"
    ),
    skip: int = Query(default=0, ge=0, description="Number of orders to skip"),
    limit: int = Query(
        default=20, ge=20, le=100, description="Maximum number of orders to return"
    ),
    session: Session = Depends(get_session),
):
    query = select(Orders)

    if order_status:
        query = query.where(Orders.status == order_status)

    if created_date:
        start = datetime.combine(created_date, datetime.min.time())

        end = datetime.combine(created_date, datetime.max.time())

        query = query.where(Orders.created_at >= start, Orders.created_at <= end)

    query = query.offset(skip).limit(limit)

    results = session.exec(query).all()

    return results


@orders_router.post(
    "/",
    response_model=Orders,
    status_code=status.HTTP_201_CREATED,
    description="Create a new order",
)
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    new_order = Orders.model_validate(order)
    session.add(new_order)
    session.commit()
    session.refresh(new_order)

    return new_order


@orders_router.get(
    "/{order_id}",
    response_model=Orders,
    status_code=status.HTTP_200_OK,
    description="Get an order by ID",
)
def get_order(order_id: int, session: Session = Depends(get_session)):
    order = session.get(Orders, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )
    return order
