from fastapi import Request, HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from .auth_services import AuthService


class BasePermission:

    def __init__(self, token_required=True):
        self.token_required = token_required

    async def __call__(self, request: Request):
        if self.token_required:
            credentials: HTTPAuthorizationCredentials = await self.get_auth_credentials(request)

            return await self.verify_credentials(credentials)
        return None

    async def get_auth_credentials(self, request: Request) -> HTTPAuthorizationCredentials:
        authorization_string: str = request.headers.get('Authorization')
        if not authorization_string:
            raise HTTPException(status_code=403, detail='Недостаточно прав доступа')
        authorization: list[str] = authorization_string.split()
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
