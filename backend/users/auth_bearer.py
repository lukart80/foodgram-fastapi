from fastapi import Request, HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from .auth_services import decode_jwt_token


class BasePermission:

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await self.get_auth_credentials(request)
        is_correct = await self.verify_credentials(credentials)

    async def get_auth_credentials(self, request: Request) -> HTTPAuthorizationCredentials:
        authorization: list[str] = request.headers.get('Authorization').split()
        if len(authorization) != 2:
            raise HTTPException(status_code=403, detail='Неверные данные авторизации.')
        return HTTPAuthorizationCredentials(scheme=authorization[0], credentials=authorization[1])

    async def verify_credentials(self, credentials: HTTPAuthorizationCredentials) -> bool:
        if credentials.scheme != 'Token':
            raise HTTPException(status_code=403, detail='Неверная схема авторизации')
        if decode_jwt_token(credentials.credentials):
            return True
        raise HTTPException(status_code=403, detail='Неверные данные авторизации')
