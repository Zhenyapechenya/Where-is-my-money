from fastapi import FastAPI, Depends

from src.auth.base_config import auth_backend, fastapi_users, current_user
from src.auth.schemas import UserRead, UserCreate
from src.auth.models import User
from src.router import router as router_money



app = FastAPI(
    title="Where i$ my money"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


app.include_router(router_money)



@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    
    return {"email": {user.email}, "salary": {user.salary}, "promotion": {user.promotion}}

@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"

