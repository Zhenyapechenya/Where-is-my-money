from fastapi_users import schemas
from typing import Optional


class UserRead(schemas.BaseUser[int]):
    # здесь нельзя выводить пароль
    id: int
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    salary: float
    promotion: str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
