from fastapi_users import schemas
from typing import Optional
from sqlalchemy import Float, TIMESTAMP
from datetime import datetime
from pydantic import BaseModel


class UserRead(BaseModel):
    # здесь нельзя выводить пароль
    id: int
    email: str
    salary: Optional[float] = None
    promotion: Optional[datetime] = None
    login_token: Optional[str] = None
    token_expires: Optional[datetime] = None

    class Config:
        orm_mode = True
        # arbitrary_types_allowed = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class TokenAdd(BaseModel):
    email: str
    hashed_password: str
    salary: Optional[float] = None
    promotion: Optional[datetime] = None
    login_token: str
    token_expires: datetime


class TokenCreate(BaseModel):
    login_token: str
    token_expires: datetime