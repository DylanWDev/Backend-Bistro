from fastapi import FastAPI
from models import Category, Cuisine, MenuItem
from sqlalchemy import Select
from routes import route

app = FastAPI()
app.include_router(route.router)

@app.get("/")
async def read_root():
    return {"msg": "hello world"}