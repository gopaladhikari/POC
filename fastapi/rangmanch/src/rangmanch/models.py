from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class Reviews(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    play_name: str = Field(index=True)
    reviwer_name: str
    rating: int = Field(..., le=5, ge=1)
    comment: str
    created_at: datetime = Field(default_factory=datetime.now)


class ReviewCreate(SQLModel):
    play_name: str
    reviwer_name: str
    rating: int = Field(..., le=5, ge=1)
    comment: str


class ReviewRead(ReviewCreate):
    id: int
    created_at: datetime


class ReviewUpdate(SQLModel):
    rating: Optional[int] = Field(default=None, le=5, ge=1)
    comment: Optional[str] = Field(default=None)
