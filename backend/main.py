from fastapi import FastAPI


from backend.routers.users import user_router
from backend.routers.ingredients import ingredients_router
from backend.routers.tags import tags_router
from backend.routers.recipes import recipes_router

app = FastAPI()


app.include_router(user_router)
app.include_router(ingredients_router)
app.include_router(tags_router)
app.include_router(recipes_router)


