from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_session
from .crud import write_user, read_all_users, read_user_by_id
from .schemas import UserOut, UserIn
from .services import hash_string

user_router = APIRouter()


@user_router.get('/users/', tags=['users'], response_model=list[UserOut])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    users = await read_all_users(session)
    return users


@user_router.post('/users/', tags=['users'], response_model=UserOut)
async def post_user(user_data: UserIn, session: AsyncSession = Depends(get_session)):
    user_data.password = hash_string(user_data.password)
    user = await write_user(session, user_data)
    return user


@user_router.get('/users/{user_id}', tags=['users'], response_model=UserOut)
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await read_user_by_id(session, user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail='Такого пользователя нет')
