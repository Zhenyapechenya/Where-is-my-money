from datetime import datetime
from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update
from pydantic.types import List

from src.database import get_async_session
from src.auth.schemas import UserRead, TokenAdd
from src.auth.models import user, User
from src.auth.base_config import auth_backend, fastapi_users, current_user
from src.auth.manager import generate_token



router = APIRouter(
    prefix="/money",
    tags=["Money"]
)

class WrongToken(Exception):
   pass

# @router.get("/{user_id}", response_model=List[UserRead])
# async def get_user_info(user_id: int, token: str, session: AsyncSession = Depends(get_async_session)):
#     try:
#         if user.login_token == None or user.token_expires < datetime.utcnow():
#             raise WrongToken("You token is wrong or expired. Please login again")
        
#         query = select(user).where((user.c.login_token == None) & (user.c.id == user_id))
#         result = await session.execute(query)
#         return result.all()
    
#     except WrongToken as e:
#         print(e)


@router.post("/get_token")
async def get_token(cur_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    new_token = generate_token()
    cur_user.login_token = new_token["token"]
    cur_user.token_expires = new_token["expires"]
    stmt = update(user).where(user.c.id == cur_user.id).values(login_token = cur_user.login_token, token_expires = cur_user.token_expires)
    await session.execute(stmt)
    await session.commit()
    return {"email": {cur_user.email}, "token": {cur_user.login_token}}


@router.post("/check_token")
async def get_money_info(token: str, user: User = Depends(current_user)):
    return {"email": {user.email}, "salary": {user.salary}, "promotion": {user.promotion}}


# @router.get("/{user_id}", response_model=List[UserRead])
# async def get_user_info(user_id: int, token: str, session: AsyncSession = Depends(get_async_session)):
#     query = select(user).where((user.c.login_token == token) & (user.c.id == user_id))
#     result = await session.execute(query)

#     return result.all()


# if user.login_token == None:
#             new_token = generate_token()
#             user.login_token = new_token["token"]
#             user.token_expires = new_token["expires"]
#             # self.add_new_token(user.id, user.login_token, user.token_expires)
#             print('1 ', user.login_token, user.token_expires, user.email)
#             # send_token_email(user.email, "user.login_token")
#         else:
#             if user.token_expires != None and user.token_expires > datetime.utcnow():
#                 # send_token_email(user.email, user.login_token)
#                 print('2 ', user.login_token, user.token_expires, user.email)
#             else: 
#                 new_token = generate_token()
#                 user.login_token = new_token["token"]
#                 user.token_expires = new_token["expires"]
#                 print('3 ', user.login_token, user.token_expires, user.email)



# if user.login_token == None:
        #     new_token = generate_token()
        #     user.login_token = new_token["token"]
        #     user.token_expires = new_token["expires"]
        #     # self.add_new_token(user.id, user.login_token, user.token_expires)
        #     print('1 ', user.login_token, user.token_expires, user.email)
        #     # send_token_email(user.email, "user.login_token")
        # else:
        #     if user.token_expires != None and user.token_expires > datetime.utcnow():
        #         # send_token_email(user.email, user.login_token)
        #         print('2 ', user.login_token, user.token_expires, user.email)
        #     else: 
        #         new_token = generate_token()
        #         user.login_token = new_token["token"]
        #         user.token_expires = new_token["expires"]
        #         print('3 ', user.login_token, user.token_expires, user.email)


        # send_token_email(user.email, user.login_token)