from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select, or_
from books_exchange.database import get_session
from books_exchange.auth import verify_api_key
from books_exchange.models.users import Users, UserCreate, ReadUser

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/", response_model=ReadUser, status_code=status.HTTP_201_CREATED)
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session),
    _: str = Depends(verify_api_key),
):
    existing_user_query = select(Users).where(
        or_(Users.email == user.email, Users.username == user.username)
    )

    existing_user = session.exec(existing_user_query).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered",
        )

    new_user = Users.model_validate(user)

    session.add(new_user)

    session.commit()

    session.refresh(new_user)

    return new_user
