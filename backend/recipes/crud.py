from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .schemas import IngredientIn, TagIn
from .models import Ingredient, Tag


async def read_all_ingredients(session: AsyncSession) -> list[Ingredient]:
    """Получить все ингредиенты."""
    result = await session.execute(select(Ingredient))

    return result.scalars().all()


async def write_ingredient(session: AsyncSession, ingredient_data: IngredientIn) -> Ingredient:
    """Создать новый ингредиент."""
    ingredient = Ingredient(**ingredient_data.dict())
    session.add(ingredient)
    await session.commit()
    await session.refresh(ingredient)
    return ingredient


async def read_all_tags(session: AsyncSession) -> list[Tag]:
    """Получить все теги."""
    result = await session.execute(select(Tag))

    return result.scalars().all()


async def write_tag(session: AsyncSession, tag_data: TagIn) -> Tag:
    """Создать тег."""
    tag = Tag(**tag_data.dict())
    session.add(tag)
    await session.commit()
    await session.refresh(tag)
    return tag
