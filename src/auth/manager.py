from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, schemas, models, exceptions

from src.auth.utils import get_user_db
from src.auth.models import User

SECRET = "SECRET" # этот ключ только для учебных целей, иначе он был бы длинным и был бы спрятан в .env и импортирован в config.py
# этот ключ отличается от ключа в файле database.py


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


    # копирую функцию из библиотеки, чтобы кастомизировать
    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        user_dict["role_id"] = 1 # по умолчанию ставлю пользователю роль user

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user



async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)