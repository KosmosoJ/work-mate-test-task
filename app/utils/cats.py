from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.models import Cat
from fastapi import HTTPException, status
from schemas import cats as cats_schema
import utils.kinds as kinds_utils


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
    
async def db_create_cat_info(cat_info:cats_schema.CreateCatSchema,
                             session:AsyncSession):
    """ Создание или получение ID породы """
    cat = Cat(kind= await kinds_utils.create_or_get_kind_id(cat_info.kind, session),
              age=cat_info.age,
              description=cat_info.description)
    session.add(cat)
    await session.commit()
    return cat