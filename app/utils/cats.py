from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.models import Cat
from fastapi import HTTPException, status


async def db_get_all_cats(session:AsyncSession):
    """ Получение всех котят """
    cats = await session.execute(select(Cat))
    cats = cats.scalars().all()
    if not cats:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return cats 

async def db_get_cat_info(id:int, session:AsyncSession):
    """ Получение информации о котенке по ID """
    cat = await session.execute(select(Cat).where(Cat.id == id))
    cat = cat.scalars().first()
    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return cat 

async def db_get_cat_by_kind(kind:str, session:AsyncSession):
    """  Получение котенка по породе  """
    #TODO Сделать поиск котенка по породе
    ...

async def db_edit_cat_info(cat_info, session:AsyncSession):
    """ Изменение информации о котенке """
    #TODO
    ...
    
async def db_delete_cat(id:int, session:AsyncSession):
    """ Удалить котенка из БД, по ID """
    #TODO
    ...
    