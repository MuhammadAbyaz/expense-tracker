from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from pymongo import MongoClient
from pymongoose import set_schemas

from .lib.schemas.schema import schemas
from .lib.database.db import connect_to_db
from .api.v1 import router
from dotenv import dotenv_values

config = dotenv_values(".env")

@asynccontextmanager
async def life_span(app:FastAPI):
    if config["DB_URL"] and config["DB_NAME"]:
        app.mongo_client: MongoClient = connect_to_db(config["DB_URL"])
        app.database = app.mongo_client[config["DB_NAME"]]
        set_schemas(app.database,schemas)
    else:
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR,"Database url or database name is missing")    
    yield
    app.mongo_client.close()

app = FastAPI(lifespan=life_span)

app.include_router(router)

@app.get("/healthcheck")
def health_check()->str:
    return "RUNNING"
