from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)

from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=True,
)

class Base(DeclarativeBase):
    pass