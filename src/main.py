from fastapi import FastAPI

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.operations.router import router as router_operation

app = FastAPI(
    title="Where i$ my money"
)


employees_db = [
    { "user_id": 1,"password": "pass1",
     "salary": 1000,"next_raise_date": (2022, 1, 1)
    },
    { "user_id": 2,"password": "pass2",
     "salary": 2000,"next_raise_date": (2023, 1, 1)
    }
]

@app.get("/user_info/{user_id}")
def get_user(user_id: int):
    return [user for user in employees_db if user.get("user_id") == user_id ]

# @app.post("/token")


@app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["Auth"],
# )

# app.include_router(router_operation)