from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from pydantic.types import List

from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import Operation


router = APIRouter(
    prefix="/info",
    tags=["User info"]
)


@router.get("/", response_model=List[Operation])
async def get_user_info(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)

    return result.all()


# @router.post("/")
# async def add_specific_operation(new_operation: Operation, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(operation).values(**new_operation.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "success"}