from pydantic import BaseModel


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
