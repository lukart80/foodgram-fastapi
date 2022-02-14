from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from backend.database.dao.ingredients import IngredientDao
from backend.database.dao.tags import TagDao
from backend.database.models.ingredients import Ingredient
from backend.database.models.tags import Tag
from backend.schemas.recipes import RecipeIn, RecipeOut, IngredientOutRecipe, IngredientInRecipe
from backend.token.manager import TokenManager
from backend.database.dao.recipes import RecipeDao
from backend.database.dao.users import UserDao
from backend.database.models.recipes import Recipe, RecipeIngredient

recipes_router = APIRouter()


@recipes_router.get('/recipes/', tags=['recipes'], response_model=list[RecipeOut])
async def get_recipes():
    recipes = await RecipeDao.read_all_objects_eager()
    results = [RecipeOut(author=recipe.author,
                         id=recipe.id,
                         tags=recipe.tags,
                         name=recipe.name,
                         image=recipe.image,
                         text=recipe.text,
                         cooking_time=recipe.cooking_time,
                         ingredients=[IngredientOutRecipe(id=recipe_ingredient.ingredient.id,
                                                          name=recipe_ingredient.ingredient.name,
                                                          measurement_unit=recipe_ingredient.ingredient.measurement_unit,
                                                          amount=recipe_ingredient.amount)
                                      for recipe_ingredient in recipe.recipe_ingredients]
                         ) for recipe in recipes]
    return results


@recipes_router.post('/recipes/', tags=['recipes'])
async def post_recipe(recipe_data: RecipeIn, user_data: dict = Depends(TokenManager())):
    recipe: Recipe = Recipe(
        author_id=user_data.get('user_id'),
        name=recipe_data.name,
        image=recipe_data.image,
        text=recipe_data.text,
        cooking_time=recipe_data.cooking_time

    )
    for tag_id in recipe_data.tags:
        tag: Tag = await TagDao.read_object_by_id(tag_id)
        if not tag:
            raise HTTPException(detail=f'Тега с id {tag_id} нет', status_code=404)
        recipe.tags.append(tag)

    for ingredient_data in recipe_data.ingredients:
        ingredient: Ingredient = await IngredientDao.read_object_by_id(ingredient_data.id)
        if not ingredient:
            raise HTTPException(detail=f'Ингридиента с id {ingredient_data.id} нет', status_code=404)
        recipe_ingredient = RecipeIngredient(recipe=recipe, ingredient=ingredient, amount=ingredient_data.amount)
        recipe.recipe_ingredients.append(recipe_ingredient)

    await UserDao.write_object(recipe)
    return {'rst': 'OK'}
