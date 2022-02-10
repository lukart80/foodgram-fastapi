from backend.database.dao.generic import GenericDao
from backend.database.models.tags import Tag


class TagDao(GenericDao):
    MODEL_CLASS = Tag
