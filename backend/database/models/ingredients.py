from sqlalchemy import Column, Integer, String

from backend.database.database import Base


class Ingredient(Base):
    """ Модель для ингредиентов."""
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    measurement_unit = Column(String, nullable=False)