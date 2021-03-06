from fastapi import APIRouter, Depends
from fastapi import HTTPException

from backend.database.models.users import User
from backend.services.users import UserService

from backend.database.dao.users import UserDao
from backend.schemas.users import UserOut, UserIn, UserLogin
from backend.services.auth import AuthService

from backend.token.manager import TokenManager

user_router = APIRouter()


@user_router.get('/users/', tags=['users'], response_model=list[UserOut])
async def get_all_users(users=Depends(UserDao.read_all_objects)):
    return users


@user_router.post('/users/', tags=['users'], response_model=UserOut)
async def post_user(user_data: UserIn):
    user = await UserService.create_user(user_data)
    return user


@user_router.get('/users/{user_id}/', tags=['users'], response_model=UserOut)
async def get_user_by_id(user_id: int):
    user = await UserDao.read_object_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail='Такого пользователя нет')


@user_router.post('/auth/token/login/')
async def check_user(credentials: UserLogin):
    user: User = await UserDao.read_user_by_credentials(credentials)
    if user:
        token = await AuthService.create_jwt_token(user.id)
        return {'auth_token': token}
    raise HTTPException(status_code=404, detail='Неверные данные пользователя.')


@user_router.post('/check/')
async def check(user_data: dict = Depends(TokenManager())):
    return {'rst': user_data}


@user_router.get('/auth/users/me/', tags=['users'], response_model=UserOut)
async def get_current_user(user_data: dict = Depends(TokenManager())):
    return await UserDao.read_object_by_id(user_data.get('user_id'))
