from fastapi import FastAPI

# from fastapi_users import FastAPIUsers
# from auth.base_config import auth_backend, fastapi_users
# from auth.schemas import UserRead, UserCreate
# from src.database import User
# from auth.manager import get_user_manager

 

app = FastAPI()


# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt",
#     tags=["auth"],
# )

# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )

@app.get("/")
def hello():
    return f"Hello"

# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.username}"

# @app.get("/unprotected-route")
# def unprotected_route():
#     return f"Hello, anonimous"