from ..db_crud import GenericDao

from .models import Ingredient, Tag


class TagDao(GenericDao):
    MODEL_CLASS = Tag


class IngredientDao(GenericDao):
    MODEL_CLASS = Ingredient
