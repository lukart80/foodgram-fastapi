from pydantic import BaseModel, Field

from backend.schemas.tags import TagOut
from backend.schemas.users import UserOut
from backend.schemas.ingredients import IngredientOut


class IngredientInRecipe(BaseModel):
    """DTO для добавления ингредиента в рецепт."""
    id: int
    amount: int


class IngredientOutRecipe(IngredientOut):
    """DTO для вывода ингредиента в рецепте."""
    amount: int

class Recipe(BaseModel):
    """Базовая DTO для рецепта."""
    name: str
    image: str
    text: str
    cooking_time: int


class RecipeIn(Recipe):
    """DTO для добавления рецепта."""
    ingredients: list[IngredientInRecipe]
    tags: list[int]


class RecipeOut(Recipe):
    """DTO вывода рецепта."""
    id: int
    tags: list[TagOut]
    author: UserOut
    ingredients: list[IngredientOutRecipe]
