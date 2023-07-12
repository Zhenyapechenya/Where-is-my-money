from datetime import datetime

from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from src.database import get_async_session
from src.auth.models import user, User
from src.auth.base_config import current_user
from src.auth.manager import generate_token, send_token_email


router = APIRouter(
    prefix="/money",
    tags=["Money"]
)

class WrongToken(Exception):
   pass
"""Error occurred during checking token."""


@router.post("/get_token")
async def get_token(cur_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    new_token = generate_token()
    cur_user.login_token = new_token["token"]
    cur_user.token_expires = new_token["expires"]
    stmt = update(user).where(user.c.id == cur_user.id).values(login_token = cur_user.login_token, token_expires = cur_user.token_expires)
    await session.execute(stmt)
    await session.commit()
    send_token_email(cur_user.email, cur_user.login_token)
    return {"email": {cur_user.email}, "token": {cur_user.login_token}}


@router.get("/money_info")
async def get_money_info(token: str, cur_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    if cur_user.login_token == None or cur_user.login_token != token or cur_user.token_expires < datetime.utcnow():
        raise WrongToken("You token is wrong or expired. Please genereate new token")

    query = select(user).where((user.c.login_token == None) & (user.c.id == cur_user.id))
    result = await session.execute(query)
    return {"email": {cur_user.email}, "salary": {cur_user.salary}, "promotion": {cur_user.promotion}}
