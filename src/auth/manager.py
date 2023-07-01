from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, schemas, models, exceptions

from src.auth.utils import get_user_db
from src.auth.models import User
from src.config import SECRET_AUTH


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH
    # verification_token_lifetime_seconds: int = 60


    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.email} has registered.")


    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

        
    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.email}. Verification token: {token}")




async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)