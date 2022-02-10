from backend.database.dao.users import UserDao
from backend.database.models.users import User
from backend.schemas.users import UserIn
from backend.utils.hash import hash_string
from backend.database.database import Base


class UserService:

    @classmethod
    async def create_user(cls, user_data: UserIn):
        user_data.password = await hash_string(user_data.password)
        user: Base = User(**user_data.dict())
        return await UserDao.write_object(user)
