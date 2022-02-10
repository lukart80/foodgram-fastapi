from pydantic import BaseModel, Field
from pydantic import EmailStr


class UserBase(BaseModel):
    """Базовый сериализатор для модели User."""
    email: EmailStr
    username: str = Field(str, max_length=30)
    first_name: str = Field(str, max_length=30)
    last_name: str = Field(str, max_length=30)

    class Config:
        orm_mode = True


class UserOut(UserBase):
    """Вывод пользователя из базы данных."""
    id: int


class UserIn(UserBase):
    """Сериализатор для создания пользователя."""
    password: str


class UserLogin(BaseModel):
    """Сериализатор для входа пользователя."""
    email: EmailStr
    password: str
