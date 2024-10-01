from fastapi import FastAPI
from routes.cats import router as cat_router
from routes.kinds import router as kind_router

app = FastAPI()

app.include_router(cat_router, tags=['cats'])
app.include_router(kind_router, tags=['kinds'])

