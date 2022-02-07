from time import time
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import jwt
from jwt.exceptions import InvalidSignatureError, DecodeError
from .models import User
from .schemas import UserLogin
from .services import hash_string

SECRET = 'super_secret!'
ALGORYTHM = 'HS256'


async def check_user_credentials(session: AsyncSession, credentials: UserLogin) -> bool:
    """Проверить корректоность данных пользователя."""
    hashed_password = hash_string(credentials.password)
    statement = select(User).filter_by(email=credentials.email, password=hashed_password)
    results = await session.execute(statement)
    return results.scalars().first() is not None


def create_jwt_token(email: str) -> str:
    """Создать токен JWT."""
    payload = {
        'email': email,
        'expires': time() + 60000
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGORYTHM)
    return token


def decode_jwt_token(token: str) -> dict:
    """Декодировать JWT токен."""
    try:
        decoded_token = jwt.decode(token, SECRET, ALGORYTHM)
        if decoded_token['expires'] < time():
            decoded_token = {}
    except (DecodeError, InvalidSignatureError):
        decoded_token = {}
    return decoded_token
