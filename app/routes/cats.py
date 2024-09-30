from fastapi import APIRouter, Depends
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from utils import cats as cats_utils

router = APIRouter(tags=['cats'])


@router.get('/cats')
async def get_all_cats(session:AsyncSession = Depends(get_session)):
    """  Получение всех котят из БД """
    cats = await cats_utils.db_get_all_cats(session)
    return {'cats': {cat.id:[cat.kind, cat.age, cat.description]} for cat in cats}