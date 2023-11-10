from fastapi import FastAPI
import models
from database import engine
from routes import route
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"msg": "hello world"}