from pydantic import BaseModel


class IngredientBase(BaseModel):
    """Базовый сериализатор для ингредиентов."""
    measurement_unit: str
    name: str

    class Config:
        orm_mode = True


class IngredientIn(IngredientBase):
    """Сериализатор для добавления ингредиента"""
    pass


class IngredientOut(IngredientBase):
    """Сериализатор для вывода ингредиента."""
    id: int
