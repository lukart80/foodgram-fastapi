from sqlalchemy.ext.asyncio import AsyncSession

from ..db_crud import write_object, read_all_objects, read_object_by_id
from .models import User
from .schemas import UserIn


async def read_all_users(session: AsyncSession) -> list[User]:
    """Получить список всех пользователей."""
    users = await read_all_objects(session, User)
    return users


async def write_user(session: AsyncSession, user_data: UserIn) -> User:
    """Создать нового пользователя."""
    user = User(**user_data.dict())
    return await write_object(session, user)


async def read_user_by_id(session: AsyncSession, user_id: int) -> User:
    """Получить пользователя по id."""
    user = await read_object_by_id(session, User, user_id)
    return user
