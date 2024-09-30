from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.models import Kind
from fastapi import HTTPException, status
from schemas import cats as cats_schema


async def create_kind(kind_name:str, session:AsyncSession):
    """ Сохранение породы в базу данных """
    kind = await session.execute(select(Kind).where(Kind.title == kind_name.lower()))
    kind = kind.scalars().first()
    if kind:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, message=f'Kind `{kind_name}` already exists')
    
    new_kind = Kind(title=kind_name.lower())
    session.add(new_kind)
    await session.commit()
    
    return new_kind

async def create_or_get_kind_id(kind_name:str, session:AsyncSession):
    kind = await session.execute(select(Kind).where(Kind.title == kind_name.lower()))
    kind = kind.scalars().first()
    
    if kind:
        return kind.id
    new_kind = Kind(title=kind_name.lower())
    session.add(new_kind)
    await session.commit()
    return new_kind.id