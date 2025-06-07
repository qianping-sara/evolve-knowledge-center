from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

def get_database_url():
    # 直接使用SQLite作为开发数据库
    return "sqlite+aiosqlite:///./app.db"

load_dotenv()
DATABASE_URL = get_database_url()
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

def get_db():
    async def _get_db():
        async with SessionLocal() as session:
            yield session
    return _get_db 