from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .schemas import IngredientIn
from .models import Ingredient


async def read_all_ingredients(db: AsyncSession) -> list[Ingredient]:
    """Получить все ингредиенты."""
    result = await db.execute(select(Ingredient))

    return result.scalars().all()


async def write_ingredient(db: AsyncSession, ingredient_data: IngredientIn) -> Ingredient:
    """Создать новый ингредиент."""
    ingredient = Ingredient(name=ingredient_data.name, measurement_unit=ingredient_data.measurement_unit)
    db.add(ingredient)
    await db.commit()
    await db.refresh(ingredient)
    return ingredient

