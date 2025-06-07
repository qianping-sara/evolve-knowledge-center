import os
from fastapi import FastAPI
from fastapi_mcp import add_mcp_server
from api.models.template_model import Base
from api.routers.template_router import router as template_router
from api.database import engine

app = FastAPI(title="Template API", description="API for Template model", version="0.1.0")

add_mcp_server(app, mount_path="/mcp", serve_tools=True)

app.include_router(template_router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
async def health():
    return {"status": "ok"} 