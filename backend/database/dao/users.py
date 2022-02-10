from sqlalchemy.future import select

from backend.utils.hash import hash_string
from backend.database.dao.generic import GenericDao
from backend.database.models.users import User
from backend.schemas.users import UserLogin


class UserDao(GenericDao):
    MODEL_CLASS = User

    @classmethod
    async def read_user_by_credentials(cls, credentials: UserLogin):
        async with cls.async_session() as session:
            async with session.begin():
                hashed_password = hash_string(credentials.password)
                statement = select(User).filter_by(email=credentials.email, password=hashed_password)
                results = await session.execute(statement)
                return results.scalars().first()
