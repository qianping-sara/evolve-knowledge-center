from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi_mcp import MCPMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from api.models.template_model import Base
from api.routers.template_router import router as template_router

def get_database_url():
    url = os.getenv("DATABASE_URL")
    if url:
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql+asyncpg://", 1)
        elif url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
        return url
    user = os.getenv("PGUSER") or os.getenv("POSTGRES_USER")
    password = os.getenv("PGPASSWORD") or os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("PGHOST") or os.getenv("POSTGRES_HOST")
    db = os.getenv("PGDATABASE") or os.getenv("POSTGRES_DATABASE")
    if user and password and host and db:
        return f"postgresql+asyncpg://{user}:{password}@{host}/{db}"
    raise RuntimeError("No valid database configuration found!")

load_dotenv()
DATABASE_URL = get_database_url()
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

def get_db():
    async def _get_db():
        async with SessionLocal() as session:
            yield session
    return _get_db

app = FastAPI(title="Template API", description="API for Template model", version="0.1.0")
app.add_middleware(MCPMiddleware)
app.include_router(template_router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
async def health():
    return {"status": "ok"} 