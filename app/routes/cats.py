from fastapi import APIRouter, Depends
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from utils import cats as cats_utils
from schemas import cats as cats_schema
from typing import Optional

router = APIRouter()


@router.get("/cats")
async def get_all_cats(
    kind: Optional[str] = None, session: AsyncSession = Depends(get_session)
):
    """Получение всех котят из БД"""
    if kind:
        cats = await cats_utils.db_get_cats_by_kind(kind, session)

    else:
        cats = await cats_utils.db_get_all_cats(session)

    return {
        "cats": [
            {
                "cat_id": cat.id,
                "cat_kind": cat.kind,
                "cat_age": cat.age,
                "cat_description": cat.description,
            }
            for cat in cats
        ]
    }


@router.get("/cat/{id}")
async def get_cat_by_id(cat_id: int, session: AsyncSession = Depends(get_session)):
    """Получение котенка из БД"""
    cat = await cats_utils.db_get_cat_info(cat_id, session)
    return {"cat_id": cat}


@router.post("/cat")
async def create_cat(
    cat_info: cats_schema.CreateCatSchema, session: AsyncSession = Depends(get_session)
):
    """Добавление котенка в базу данных"""
    cat = await cats_utils.db_create_cat_info(cat_info, session)
    return cat


@router.put("/cat/{id}")
async def edit_cat(
    cat_id: int,
    cat_info: cats_schema.CatSchema,
    session: AsyncSession = Depends(get_session),
):
    """Изменение информации о котенке по ID"""
    cat = await cats_utils.db_edit_cat_info(cat_id, cat_info, session)
    return cat


@router.delete("/cat/{id}")
async def delete_cat(cat_id: int, session: AsyncSession = Depends(get_session)):
    """Удаление котенка по ID"""
    cat = await cats_utils.db_delete_cat(cat_id, session)
    return cat
