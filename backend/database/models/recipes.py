from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.database.database import Base


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    tags = relationship('Tag', secondary='recipe_tags', back_populates='recipes')
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='recipes')
    recipe_ingredients = relationship('RecipeIngredient', back_populates='recipe')
    name = Column(String)
    image = Column(String)
    text = Column(String)
    cooking_time = Column(Integer)


class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship('Recipe', back_populates='recipe_ingredients')
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    ingredient = relationship('Ingredient', back_populates='recipe_ingredients')
    amount = Column(Integer)


class RecipeTags(Base):
    __tablename__ = 'recipe_tags'

    id = Column(Integer, primary_key=True, index=True)
    tag_id = Column(Integer, ForeignKey('tags.id'))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
