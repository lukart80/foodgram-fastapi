from fastapi import FastAPI

from .recipes.routers import recipe_router
from .users.routers import user_router
app = FastAPI()

app.include_router(recipe_router)
app.include_router(user_router)



