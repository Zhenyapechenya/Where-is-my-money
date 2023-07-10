from fastapi_users import schemas
from typing import Optional
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


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
