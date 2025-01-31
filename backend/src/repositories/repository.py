from src.schemas.schemas import CarParts
from src.schemas.schemas import CarMileage
from src.config.db.session import async_session_maker
from sqlalchemy import select
from src.models.models import PartsModels


class CarPartsRepository:
    @classmethod
    async def find_all(cls, request: CarMileage) -> list[CarParts]:
        async with async_session_maker() as session:
            try:
                query = select(PartsModels)
                result = await session.execute(query)
                parts = result.scalars().all()
                print(parts)
                if not parts:
                    return []
                return [CarParts.model_validate(part.__dict__) for part in parts]
            except Exception as e:
                print(f"Error in CarPartsRepository.find_all: {e}")
                return []