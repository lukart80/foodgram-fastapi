from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from backend.database.dao.generic import GenericDao

from backend.database.models.recipes import Recipe
from backend.database.models.recipes import RecipeIngredient


class RecipeDao(GenericDao):
    MODEL_CLASS = Recipe

    @classmethod
    async def read_all_objects_eager(cls) -> list[Recipe]:
        async with cls.async_session() as session:
            statement = select(cls.MODEL_CLASS).options(joinedload(cls.MODEL_CLASS.author),
                                                        joinedload(cls.MODEL_CLASS.tags),
                                                        joinedload(cls.MODEL_CLASS.recipe_ingredients).subqueryload(
                                                            RecipeIngredient.ingredient)
                                                        )
            results = await session.execute(statement)
            await session.commit()
        return results.unique().scalars().all()

    @classmethod
    async def read_object_by_id_eager(cls, object_id: int) -> Recipe:
        async with cls.async_session() as session:
            statement = select(cls.MODEL_CLASS).filter_by(id=object_id).options(joinedload(cls.MODEL_CLASS.author),
                                                        joinedload(cls.MODEL_CLASS.tags),
                                                        joinedload(
                                                            cls.MODEL_CLASS.recipe_ingredients).subqueryload(
                                                            RecipeIngredient.ingredient)
                                                        )
            results = await session.execute(statement)
            await session.commit()
        return results.unique().scalars().first()
