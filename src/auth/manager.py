from typing import Optional
import smtplib, ssl
import string
from random import choices
from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Request, Response
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas
from pydantic import EmailStr

from src.auth.models import User
from src.auth.utils import get_user_db
from src.config import SECRET_AUTH, SMTP_HOST, SMTP_PASSWORD, SMTP_PORT, SMTP_USERNAME, SENDER_EMAIL
from src.database import get_async_session



def generate_token():
    expires_delta = timedelta(hours=1)
    expires_date = datetime.utcnow() + expires_delta
    token = {
        "expires": expires_date,
        "token": str(''.join(choices(string.ascii_uppercase + string.digits, k = 10)))
    }
    return token

def send_token_email(email: EmailStr, token: str):
    message = f'{token}'
    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(SENDER_EMAIL, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, email, message)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH

    async def on_after_login(
        self,
        user: User,
        request: Optional[Request] = None,
        response: Optional[Response] = None,
        session: AsyncSession = Depends(get_async_session)
    ):
        print(f"User {user.email} logged in.")
        

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


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
        user_dict["promotion"] = datetime.utcnow() + timedelta(days=90)

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)
        
        return created_user
    

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
