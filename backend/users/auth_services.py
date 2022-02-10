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


class AuthService:

    @classmethod
    async def create_jwt_token(cls, user_id: int) -> str:
        """Создать jwt токен пользователя."""
        payload = {
            'user_id': user_id,
            'expires': time() + 60000
        }
        token = jwt.encode(payload, SECRET, algorithm=ALGORYTHM)
        return token

    @classmethod
    async def decode_jwt_token(cls, token: str) -> dict:
        """Декодировать JWT токен."""
        try:
            decoded_token = jwt.decode(token, SECRET, ALGORYTHM)
            if decoded_token['expires'] < time():
                decoded_token = {}
        except (DecodeError, InvalidSignatureError):
            decoded_token = {}
        return decoded_token
