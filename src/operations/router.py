from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic.types import List

from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import Operation

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.get("/", response_model=List[Operation])
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    print(query)
    result = await session.execute(query)

    return result.all()