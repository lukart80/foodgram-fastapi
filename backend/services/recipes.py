from backend.database.models.recipes import Recipe
from backend.schemas.recipes import RecipeOut, IngredientOutRecipe


class RecipeServices:

    @staticmethod
    async def generate_response_dto(recipe: Recipe) -> RecipeOut:
        return RecipeOut(author=recipe.author,
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
                         )
