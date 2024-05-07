

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .configurations.db import database
from .users.models.user_entity import users


app = FastAPI()
app.title = 'migration exercise'
app.version = '0.0.1'

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/', tags=['home'])
def message():
    # RETORNA el hatml
    return HTMLResponse('<h1>Holas</h1>')

@app.get("/users")
async def find_all_books():
    query = users.select()
    return await database.fetch_all(query)