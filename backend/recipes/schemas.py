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


class TagBase(BaseModel):
    """Базовый сериализатор для тегов."""
    name: str
    color: str

    class Config:
        orm_mode = True


class TagIn(TagBase):
    """Сериализатор для добавления тега."""
    pass


class TagOut(TagBase):
    """Сериализатор для получение ингредиента."""
    id: int
