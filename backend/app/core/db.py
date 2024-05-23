
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from core.config import get_api_settings

settings = get_api_settings()

async_engine = create_async_engine(
   settings.db_async_connection_str,
   echo=True,
   future=True
)

async def get_async_session() -> AsyncSession:
   async_session = sessionmaker(
       bind=async_engine, class_=AsyncSession, expire_on_commit=False
   )
   async with async_session() as session:
       yield session