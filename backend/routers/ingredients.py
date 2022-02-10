from fastapi import APIRouter
from fastapi import HTTPException

from backend.database.dao.ingredients import IngredientDao
from backend.database.models.ingredients import Ingredient
from backend.schemas.ingredients import IngredientOut, IngredientIn

ingredients_router = APIRouter()


@ingredients_router.get('/ingredients/', tags=['ingredients'], response_model=list[IngredientOut])
async def get_ingredients():
    ingredients = await IngredientDao.read_all_objects()
    return ingredients


@ingredients_router.post('/ingredients/', tags=['ingredients'], response_model=IngredientOut)
async def post_ingredient(ingredient_data: IngredientIn):
    ingredient = await IngredientDao.write_object(Ingredient(**ingredient_data.dict()))
    return ingredient


@ingredients_router.get('/ingredients/{ingredient_id}', tags=['ingredients'], response_model=IngredientOut)
async def get_ingredient_by_id(ingredient_id: int):
    ingredient = await IngredientDao.read_object_by_id(ingredient_id)
    if ingredient:
        return ingredient
    raise HTTPException(status_code=404, detail='Ингредиент не найден')
