from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..db_crud import write_object, read_all_objects, read_object_by_id
from .schemas import IngredientIn, TagIn
from .models import Ingredient, Tag


async def read_all_ingredients(session: AsyncSession) -> list[Ingredient]:
    """Получить все ингредиенты."""
    result = await read_all_objects(session, Ingredient)
    return result


async def write_ingredient(session: AsyncSession, ingredient_data: IngredientIn) -> Ingredient:
    """Создать новый ингредиент."""
    ingredient = await write_object(session, Ingredient, ingredient_data)

    return ingredient


async def read_ingredient_by_id(session: AsyncSession, ingredient_id: int) -> Ingredient:
    """Получить ингредиент по id."""
    ingredient = await read_object_by_id(session, Ingredient, ingredient_id)
    return ingredient


async def read_all_tags(session: AsyncSession) -> list[Tag]:
    """Получить все теги."""
    result = await read_all_objects(session, Tag)

    return result


async def read_tag_by_id(session: AsyncSession, tag_id: int) -> Tag:
    """Получить тег по id."""
    tag = await read_object_by_id(session, Tag, tag_id)
    return tag


async def write_tag(session: AsyncSession, tag_data: TagIn) -> Tag:
    """Создать тег."""
    tag = await write_object(session, Tag, tag_data)
    return tag
