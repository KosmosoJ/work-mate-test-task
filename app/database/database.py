from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from os import environ
from dotenv import find_dotenv, load_dotenv

if find_dotenv():
    load_dotenv()
    database_url = environ.get('DATABASE_URL')
    
engine = create_async_engine(database_url, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    ...

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session