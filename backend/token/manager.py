from fastapi import Request, HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from backend.services.auth import AuthService


class TokenManager:
    """Позволяет получить декодированный токен из HTTP заголовка Authorization. Если параметр token_required=False,
     при пустом загаловке вернется None."""

    def __init__(self, token_required=True):
        self.token_required = token_required

    async def __call__(self, request: Request):
        credentials_string: str = request.headers.get('Authorization')
        if not self.token_required and credentials_string is None:
            return None

        credentials: HTTPAuthorizationCredentials = await self.parse_credentials_string(credentials_string)
        return await self.verify_credentials(credentials)

    async def parse_credentials_string(self, credentials_string: str) -> HTTPAuthorizationCredentials:
        if not credentials_string:
            raise HTTPException(status_code=403, detail='Недостаточно прав доступа')
        authorization: list[str] = credentials_string.split()
        if len(authorization) != 2:
            raise HTTPException(status_code=403, detail='Неверные данные авторизации.')
        return HTTPAuthorizationCredentials(scheme=authorization[0], credentials=authorization[1])

    async def verify_credentials(self, credentials: HTTPAuthorizationCredentials) -> dict:
        if credentials.scheme != 'Token':
            raise HTTPException(status_code=403, detail='Неверная схема авторизации')
        decoded_token = await AuthService.decode_jwt_token(credentials.credentials)
        if decoded_token:
            return decoded_token
        raise HTTPException(status_code=403, detail='Неверные данные авторизации')
