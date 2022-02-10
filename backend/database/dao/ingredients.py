from backend.database.dao.generic import GenericDao
from backend.database.models.ingredients import Ingredient


class IngredientDao(GenericDao):
    MODEL_CLASS = Ingredient
