from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/tada_db2"


engine = AsyncEngine(create_engine(DATABASE_URL, echo=True, future=True))

