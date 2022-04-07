from typing import Optional
import uvicorn
from fastapi import FastAPI
from environs import Env

env = Env()
env.read_env()
secret = env.str("APP_SECRET_STRING", "DEFAULT")
item = env.str("APP_ITEM_VALUE", "DEFAULT")
port = env.int("APP_PORT", 80)

app = FastAPI()


@app.get("/")   
def root():
    return {"message": "All good!"}


@app.get("/secrets")
def read_item():
    return {"message": secret}


@app.get("/items")
def read_item():
    return {"message": item}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
    )
