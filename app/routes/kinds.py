from fastapi import APIRouter, Depends
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
import utils.kinds as kind_utils
import schemas.kinds as kind_schema

router = APIRouter()

@router.get('/kinds', response_model=list[kind_schema.KindBase])
async def get_all_kinds(session:AsyncSession = Depends(get_session)):
    """ Получение информации о всех породах """
    
    kinds = await kind_utils.get_all_kinds(session)
    return [{'id':kind.id, 'title':kind.title} for kind in kinds]