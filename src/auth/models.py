from typing import Optional
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Column, Float, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from datetime import datetime

from src.database import Base


metadata = MetaData()


user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("email", String, nullable=False), 
    # Column("username", String, nullable=False), 
    # Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    # Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=True, nullable=False),
    Column("salary", Float), # этот столбец не может быть пустым
    Column("promotion", TIMESTAMP),  
    Column("login_token",  String),
    Column("token_expires", TIMESTAMP),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    # username = Column(String, nullable=False)
    # registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    # role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    salary: Optional[Float] = Column(Float, nullable=False)
    promotion: Optional[TIMESTAMP] = Column(TIMESTAMP)
    login_token: str = Column(String(length=50))
    token_expires = Column(TIMESTAMP)
