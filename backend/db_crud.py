from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from .database import Base


async def read_all_objects(session: AsyncSession, model: Base) -> list[Base]:
    """Получить все объекты модели"""
    results = await session.execute(select(model))
    return results.scalars().all()


async def write_object(session: AsyncSession, model: Base, data: BaseModel) -> Base:
    """Создать объект модели."""
    model_object = model(**data.dict())
    session.add(model_object)
    await session.commit()
    await session.refresh(model_object)
    return model_object


async def read_object_by_id(session: AsyncSession, model: Base, object_id: int) -> Base:
    """Получить объект модели по id."""
    statement = select(model).filter_by(id=object_id)
    results = await session.execute(statement)
    return results.scalars().first()
