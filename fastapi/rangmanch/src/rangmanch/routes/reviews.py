from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import Session, select, func, col
from rangmanch.models import Reviews, ReviewCreate, ReviewRead, ReviewUpdate
from rangmanch.database import get_session
from typing import Optional

reviews_router = APIRouter(prefix="/reviews", tags=["reviews"])


@reviews_router.post("/", response_model=ReviewRead, description="Create a new review")
def create_review(review: ReviewCreate, session: Session = Depends(get_session)):
    db_review = Reviews.model_validate(review)

    session.add(db_review)
    session.commit()
    session.refresh(db_review)

    return db_review


@reviews_router.get(
    "/", response_model=list[ReviewRead], description="Get all paginated reviews"
)
def get_reviews(
    play_name: Optional[str] = Query(None, description="Filter by play name"),
    limit: int = Query(10, ge=1, le=100, description="Number of reviews per page"),
    skip: int = Query(0, ge=0, description="Skip number of reviews"),
    session: Session = Depends(get_session),
):
    query = select(Reviews)

    if play_name:
        query = query.where(Reviews.play_name == play_name)

    query = query.offset(skip).limit(limit)

    reviews = session.exec(query).all()

    return reviews


@reviews_router.get("/average/{play_name}")
def get_average_rating(play_name: str, session: Session = Depends(get_session)):

    query = select(func.avg(Reviews.rating), func.count(col(Reviews.id))).where(
        Reviews.play_name == play_name
    )

    result = session.exec(query).first()

    if not result:
        raise HTTPException(status_code=404, detail="Review not found")

    average_rating, total_reviews = result

    return {
        "play_name": play_name,
        "average_rating": round(average_rating, 2),
        "totle_reviews": total_reviews,
    }


@reviews_router.get("/{review_id}", response_model=ReviewRead)
def get_review(review_id: int, session: Session = Depends(get_session)):
    review = session.get(Reviews, review_id)

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    return review


@reviews_router.put("/{review_id}", response_model=ReviewRead)
def update_review(
    review_id: int,
    review: ReviewUpdate,
    session: Session = Depends(get_session),
):
    db_review = session.get(Reviews, review_id)

    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")

    incoming_data = review.model_dump(exclude_unset=True)

    for key, value in incoming_data.items():
        setattr(db_review, key, value)

    session.add(db_review)
    session.commit()
    session.refresh(db_review)

    return db_review


@reviews_router.delete("/{review_id}")
def delete_review(review_id: int, session: Session = Depends(get_session)):
    review = session.get(Reviews, review_id)

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    session.delete(review)
    session.commit()

    return {"message": "Review deleted"}
