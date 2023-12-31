from typing import Optional
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Column, Float, Integer, String, TIMESTAMP, Boolean

from src.database import Base


metadata = MetaData()


user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("email", String, nullable=False), 
    Column("hashed_password", String, nullable=False),
    Column("salary", Float),
    Column("promotion", TIMESTAMP),  
    Column("login_token",  String),
    Column("token_expires", TIMESTAMP),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=True, nullable=False),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    salary: Optional[Float] = Column(Float, nullable=False)
    promotion: Optional[TIMESTAMP] = Column(TIMESTAMP)
    login_token: str = Column(String(length=50))
    token_expires = Column(TIMESTAMP)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
