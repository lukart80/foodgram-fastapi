from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from sqlalchemy.orm import sessionmaker

from .database import Base, engine


class GenericDao:
    MODEL_CLASS: Base = None
    async_session: AsyncSession = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    @classmethod
    async def read_all_objects(cls) -> list[Base]:
        """Получить все объекты модели."""

        async with cls.async_session() as session:
            results = await session.execute(select(cls.MODEL_CLASS))
            await session.commit()
        return results.scalars().all()

    @classmethod
    async def write_object(cls, model: Base) -> Base:
        """Сохранить модель в базу данных."""
        async with cls.async_session() as session:
            async with session.begin():
                session.add(model)

                await session.commit()

        return model

    @classmethod
    async def read_object_by_id(cls, object_id: int) -> Base:
        """Получить объект по id."""
        async with cls.async_session() as session:
            async with session.begin():
                statement = select(cls.MODEL_CLASS).filter_by(id=object_id)
                results = await session.execute(statement)
                await session.commit()
        return results.scalars().first()
