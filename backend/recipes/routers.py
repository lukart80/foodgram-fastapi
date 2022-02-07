from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_session
from .schemas import IngredientOut, IngredientIn
from .crud import read_all_ingredients, write_ingredient

recipe_router = APIRouter()


@recipe_router.get('/ingredients/', tags=['ingredients'], response_model=list[IngredientOut])
async def get_ingredients(session: AsyncSession = Depends(get_session)):
    ingredients = await read_all_ingredients(session)
    return ingredients


@recipe_router.post('/ingredients/', tags=['ingredients'], response_model=IngredientOut)
async def post_ingredient(ingredient_data: IngredientIn, session: AsyncSession = Depends(get_session)):
    ingredient = await write_ingredient(session, ingredient_data)
    return ingredient
