import random
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from .cats import db_get_all_cats, db_create_cat_info
from schemas.cats import CreateCatSchema
from database.database import get_session
from contextlib import asynccontextmanager


get_async_session_context = asynccontextmanager(get_session)


async def create_init_data():
    """ Внесение базовых данных в БД """
    
    kinds = ['Британец', 'Сиамский', 'Дворняжка', 'Бурма', 'Сфинкс']
    descriptions = ['Сиамская кошка — одна из известных пород кошек сиамо-ориентальной группы.','бурманская короткошёрстная кошка — порода короткошёрстных кошек. Кошку бурманской породы отличает мускулистое, ' , 'милый котеночек ^_^', 'Нашли под деревом, ищет свой домик', 'Очень любит руки']
    async with get_async_session_context() as session:
        try:
            if not await db_get_all_cats(session):
                ...
        except HTTPException:
            for i in range(10):
                cat = CreateCatSchema(kind=random.choice(kinds), age=random.randint(1,12), description=random.choice(descriptions))
                await db_create_cat_info(cat, session)
        