from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.models import Cat, Kind
from fastapi import HTTPException, status
from schemas import cats as cats_schema
import utils.kinds as kinds_utils


async def db_get_all_cats(session: AsyncSession):
    """Получение всех котят"""
    cats = await session.execute(select(Cat))
    cats = cats.scalars().all()
    if not cats:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return cats


async def db_get_cats_by_kind(search_kind: str, session: AsyncSession):
    """Поиск котят по породе"""
    subquery = (
        select(Kind.id).where(Kind.title.contains(search_kind.lower())).subquery()
    )
    cats = await session.execute(select(Cat).where(Cat.kind.in_(subquery)))
    cats = cats.scalars().all()
    if not cats:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cats not found"
        )
    return cats


async def db_get_cat_info(cat_id: int, session: AsyncSession):
    """Получение информации о котенке по ID"""
    cat = await session.execute(select(Cat).where(Cat.id == cat_id))
    cat = cat.scalars().first()
    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return cat


async def db_edit_cat_info(
    cat_id: int, cat_info: cats_schema.CreateCatSchema, session: AsyncSession
):
    """Изменение информации о котенке"""
    cat = await session.execute(select(Cat).where(Cat.id == cat_id))
    cat = cat.scalars().first()

    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    cat.kind, cat.age, cat.color, cat.description = (
        await kinds_utils.create_or_get_kind_id(cat_info.kind, session),
        cat_info.age,
        cat_info.color,
        cat_info.description,
    )

    await session.commit()
    return cat


async def db_delete_cat(cat_id: int, session: AsyncSession):
    """Удалить котенка из БД, по ID"""
    cat = await session.execute(select(Cat).where(Cat.id == cat_id))
    cat = cat.scalars().first()

    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    await session.delete(cat)
    await session.commit()
    return cat


async def db_create_cat_info(
    cat_info: cats_schema.CreateCatSchema, session: AsyncSession
):
    """Создание информации о котенке"""
    cat = Cat(
        kind=await kinds_utils.create_or_get_kind_id(cat_info.kind, session),
        age=cat_info.age,
        color=cat_info.color,
        description=cat_info.description,
    )
    session.add(cat)
    await session.commit()
    return cat
