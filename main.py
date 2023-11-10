from fastapi import FastAPI
import models
from database import engine
from routes import route
import enum
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(route.router)

@app.get("/")
async def read_root():
    return {"msg": "hello world"}