from fastapi import APIRouter, Depends
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
import utils.kinds as kind_utils

router = APIRouter()

@router.get('/kinds')
async def get_all_kinds(session:AsyncSession = Depends(get_session)):
    """ Получение информации о всех породах """
    
    kinds = await kind_utils.get_all_kinds(session)
    return [{'id':kind.id, 'title':kind.title} for kind in kinds]