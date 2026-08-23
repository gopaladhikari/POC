from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select, func, col
from datetime import datetime, date
from delivery.models import Orders, StatusLog, OrderStatus
from delivery.database import get_session
from typing import Optional

stats_router = APIRouter(prefix="/stats", tags=["Stats"])


@stats_router.get("/daily")
def get_daily_stats(
    summary_date: Optional[date] = Query(
        None, description="Date for which to get the statistics"
    ),
    session: Session = Depends(get_session),
):
    if not summary_date:
        summary_date = date.today()

    start = datetime.combine(summary_date, datetime.min.time())
    end = datetime.combine(summary_date, datetime.max.time())

    summary = {}
    total = 0

    for status in OrderStatus:
        query = select(func.count(col(Orders.id))).where(
            Orders.status == status,
            Orders.created_at >= start,
            Orders.created_at <= end,
        )

        count = session.exec(query).one()

        summary[status.value] = count
        total += count

    return {
        "date": summary_date.isoformat(),
        "summary": summary,
        "total_orders": total,
    }
