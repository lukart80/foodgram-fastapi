from fastapi import APIRouter, HTTPException

from backend.database.dao.tags import TagDao
from backend.database.models.tags import Tag
from backend.schemas.tags import TagOut, TagIn

tags_router = APIRouter()


@tags_router.get('/tags/', tags=['tags'], response_model=list[TagOut])
async def get_tags():
    tags = await TagDao.read_all_objects()
    return tags


@tags_router.post('/tags/', tags=['tags'], response_model=TagOut)
async def post_tag(tag_data: TagIn):
    tag = await TagDao.write_object(Tag(**tag_data.dict()))
    return tag


@tags_router.get('/tags/{tag_id}/', tags=['tags'], response_model=TagOut)
async def get_tag_by_id(tag_id: int):
    tag = await TagDao.read_object_by_id(tag_id)
    if tag:
        return tag
    raise HTTPException(status_code=404, detail='Тег не найден')
