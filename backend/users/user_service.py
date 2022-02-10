from .crud import UserDao
from .models import User
from .schemas import UserIn
from .services import hash_string
from ..database import Base


class UserService:

    @classmethod
    async def create_user(cls, user_data: UserIn):
        user_data.password = hash_string(user_data.password)
        user: Base = User(**user_data.dict())
        return await UserDao.write_object(user)
