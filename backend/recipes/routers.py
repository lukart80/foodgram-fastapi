from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_session
from .schemas import IngredientOut, IngredientIn, TagOut, TagIn
from .crud import read_all_ingredients, write_ingredient, read_all_tags, write_tag, read_tag_by_id, read_ingredient_by_id


recipe_router = APIRouter()


@recipe_router.get('/ingredients/', tags=['ingredients'], response_model=list[IngredientOut])
async def get_ingredients(session: AsyncSession = Depends(get_session)):
    ingredients = await read_all_ingredients(session)
    return ingredients


@recipe_router.post('/ingredients/', tags=['ingredients'], response_model=IngredientOut)
async def post_ingredient(ingredient_data: IngredientIn, session: AsyncSession = Depends(get_session)):
    ingredient = await write_ingredient(session, ingredient_data)
    return ingredient


@recipe_router.get('/ingredients/{ingredient_id}', tags=['ingredients'], response_model=IngredientOut)
async def get_ingredient_by_id(ingredient_id: int, session: AsyncSession = Depends(get_session)):
    ingredient = await read_ingredient_by_id(session, ingredient_id)
    if ingredient:
        return ingredient
    raise HTTPException(status_code=404, detail='Ингредиент не найден')


@recipe_router.get('/tags/', tags=['tags'], response_model=list[TagOut])
async def get_tags(session: AsyncSession = Depends(get_session)):
    tags = await read_all_tags(session)
    return tags


@recipe_router.post('/tags/', tags=['tags'], response_model=TagOut)
async def post_tag(tag_data: TagIn, session: AsyncSession = Depends(get_session)):
    tag = await write_tag(session, tag_data)
    return tag


@recipe_router.get('/tags/{tag_id}/', tags=['tags'], response_model=TagOut)
async def get_tag_by_id(tag_id: int, session: AsyncSession = Depends(get_session)):
    tag = await read_tag_by_id(session, tag_id)
    if tag:
        return tag
    raise HTTPException(status_code=404, detail='Тег не найден')
