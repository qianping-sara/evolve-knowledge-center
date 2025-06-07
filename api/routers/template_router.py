from fastapi import APIRouter, Depends, HTTPException
from fastapi_mcp import mcp_api
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.template_schema import TemplateCreate, TemplateRead
from api.services.template_service import TemplateService
from api.main import get_db
from typing import List

router = APIRouter(prefix="/templates", tags=["Template"])

@mcp_api(router, "/", methods=["POST"], response_model=TemplateRead)
async def create_template(template: TemplateCreate, db: AsyncSession = Depends(get_db)):
    return await TemplateService.create_template(db, template)

@mcp_api(router, "/", methods=["GET"], response_model=List[TemplateRead])
async def list_templates(db: AsyncSession = Depends(get_db)):
    return await TemplateService.list_templates(db)

@mcp_api(router, "/{template_id}", methods=["GET"], response_model=TemplateRead)
async def get_template(template_id: str, db: AsyncSession = Depends(get_db)):
    obj = await TemplateService.get_template(db, template_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Template not found")
    return obj

@mcp_api(router, "/{template_id}", methods=["PUT"], response_model=TemplateRead)
async def update_template(template_id: str, template: TemplateCreate, db: AsyncSession = Depends(get_db)):
    obj = await TemplateService.update_template(db, template_id, template)
    if not obj:
        raise HTTPException(status_code=404, detail="Template not found")
    return obj

@mcp_api(router, "/{template_id}", methods=["DELETE"])
async def delete_template(template_id: str, db: AsyncSession = Depends(get_db)):
    ok = await TemplateService.delete_template(db, template_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Template not found")
    return {"ok": True} 