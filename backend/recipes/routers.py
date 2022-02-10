from fastapi import APIRouter
from fastapi import HTTPException

from .models import Ingredient, Tag
from .schemas import IngredientOut, IngredientIn, TagOut, TagIn
from .crud import IngredientDao, TagDao


recipe_router = APIRouter()


@recipe_router.get('/ingredients/', tags=['ingredients'], response_model=list[IngredientOut])
async def get_ingredients():
    ingredients = await IngredientDao.read_all_objects()
    return ingredients


@recipe_router.post('/ingredients/', tags=['ingredients'], response_model=IngredientOut)
async def post_ingredient(ingredient_data: IngredientIn):
    ingredient = await IngredientDao.write_object(Ingredient(**ingredient_data.dict()))
    return ingredient


@recipe_router.get('/ingredients/{ingredient_id}', tags=['ingredients'], response_model=IngredientOut)
async def get_ingredient_by_id(ingredient_id: int):
    ingredient = await IngredientDao.read_object_by_id(ingredient_id)
    if ingredient:
        return ingredient
    raise HTTPException(status_code=404, detail='Ингредиент не найден')


@recipe_router.get('/tags/', tags=['tags'], response_model=list[TagOut])
async def get_tags():
    tags = await TagDao.read_all_objects()
    return tags


@recipe_router.post('/tags/', tags=['tags'], response_model=TagOut)
async def post_tag(tag_data: TagIn):
    tag = await TagDao.write_object(Tag(**tag_data.dict()))
    return tag


@recipe_router.get('/tags/{tag_id}/', tags=['tags'], response_model=TagOut)
async def get_tag_by_id(tag_id: int):
    tag = await TagDao.read_object_by_id(tag_id)
    if tag:
        return tag
    raise HTTPException(status_code=404, detail='Тег не найден')
