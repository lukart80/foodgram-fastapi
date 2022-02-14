from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.database.database import Base


class Tag(Base):
    """Модель для тегов."""
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    color = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    recipes = relationship('Recipe', secondary='recipe_tags', back_populates='tags')
