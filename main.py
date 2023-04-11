from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


app = FastAPI(
    title="Traiding App"
)



fake_users = [
    {"id": 1, "role": "admin", "name": ["Bob"]},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
    {"id": 4, "role": "investor", "name": "Homer", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
    ]},
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]

plants = [
    {"id": 1, "type": "leaf", "name": "Billy"},
    {"id": 2, "type": "bloom", "name": "Antony"},
    {"id": 3, "type": "cactus", "name": "Cassy"},
]



class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = [] # указала, что параметр необязательный, звание может отсутствовать




@app.get("/users/{user_id}", response_model=List[User]) # дополнительно указываю модель данных, которыми отвечает ф-я
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

@app.get("/plants/{plant_id}")
def get_user(plant_id: int):
    return [plant for plant in plants if plant.get("id") == plant_id]






class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=6) # установила ограничение: не длиннее 5 символов
    side: str
    price: float = Field(ge=0) # установила ограничение: больше, чем 0
    amount: float


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}
    

    


