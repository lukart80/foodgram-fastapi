from fastapi import FastAPI
from .database import init_db

app = FastAPI()


@app.on_event('startup')
async def on_startup():
    await init_db()
