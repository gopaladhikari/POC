from pydantic import BaseModel, EmailStr
from uuid import UUID


class User(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: str | None = None

    def get_uid(self) -> UUID | None:
        if self.user_id:
            return UUID(self.user_id)
        return None
