from pydantic import BaseModel
from datetime import datetime


class Operation(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    type: str
    date: datetime

    class Config:
        orm_mode = True

