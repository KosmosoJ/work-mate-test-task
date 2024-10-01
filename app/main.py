from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from routes.cats import router as cat_router
from routes.kinds import router as kind_router
from database.database import get_session
from contextlib import asynccontextmanager

from utils.init_db_data import create_init_data



@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_init_data()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(cat_router, tags=['cats'])
app.include_router(kind_router, tags=['kinds'])



    