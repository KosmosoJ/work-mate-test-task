from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.models import Kind
from fastapi import HTTPException, status


async def create_kind(kind_name: str, session: AsyncSession):
    """Сохранение породы в базу данных"""
    kind = await session.execute(select(Kind).where(Kind.title == kind_name.lower()))
    kind = kind.scalars().first()
    if kind:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Kind `{kind_name}` already exists",
        )

    new_kind = Kind(title=kind_name.lower())
    session.add(new_kind)
    await session.commit()

    return new_kind


async def create_or_get_kind_id(kind_name: str, session: AsyncSession):
    """Создание или получение ID породы по названию породы"""
    kind = await session.execute(select(Kind).where(Kind.title == kind_name.lower()))
    kind = kind.scalars().first()

    if kind:
        return kind.id
    new_kind = Kind(title=kind_name.lower())
    session.add(new_kind)
    await session.commit()
    return new_kind.id


async def get_all_kinds(session: AsyncSession):
    """Получение всех пород из БД"""
    kinds = await session.execute(select(Kind))
    kinds = kinds.scalars().all()
    if not kinds:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return kinds
