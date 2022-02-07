from fastapi import FastAPI

from .recipes.routers import recipe_router
app = FastAPI()

app.include_router(recipe_router)



