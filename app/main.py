from fastapi import FastAPI
from routes.cats import router as cat_router

app = FastAPI()

app.include_router(cat_router, tags=['cats'])