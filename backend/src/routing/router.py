from fastapi import APIRouter
from src.schemas.schemas import CarMileage
from src.repositories.repository import CarPartsRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from src.config.db.session import get_async_session
from src.schemas.schemas import CarParts


router = APIRouter(
    prefix="/api",
)


@router.get("/parts")
async def get_parts():
    return {"message": "Ура получил ответ от сервера"}


@router.post("/get_num")
async def get_num(request: CarMileage, 
                  db: AsyncSession = Depends(get_async_session)) -> list[CarParts]:
    parts = await CarPartsRepository.find_all(request)
    print(parts)
    return parts