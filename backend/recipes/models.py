from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, Column

Base = declarative_base()


class Ingredient(Base):
    """ Модель для ингредиентов."""
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    measurement_unit = Column(String, nullable=False)
