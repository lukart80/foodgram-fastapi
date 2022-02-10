from sqlalchemy import Column, Integer, String

from backend.database.database import Base


class Tag(Base):
    """Модель для тегов."""
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    color = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
