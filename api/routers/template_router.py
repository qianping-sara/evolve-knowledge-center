from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.template_schema import TemplateCreate, TemplateRead
from api.services.template_service import TemplateService
from api.database import get_db
from typing import List

router = APIRouter(prefix="/templates", tags=["Template"])

@router.post("/", response_model=TemplateRead)
async def create_template(template: TemplateCreate, db: AsyncSession = Depends(get_db())):
    return await TemplateService.create_template(db, template)

@router.get("/", response_model=List[TemplateRead])
async def list_templates(db: AsyncSession = Depends(get_db())):
    return await TemplateService.list_templates(db)

@router.get("/{template_id}", response_model=TemplateRead)
async def get_template(template_id: str, db: AsyncSession = Depends(get_db())):
    obj = await TemplateService.get_template(db, template_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Template not found")
    return obj

@router.put("/{template_id}", response_model=TemplateRead)
async def update_template(template_id: str, template: TemplateCreate, db: AsyncSession = Depends(get_db())):
    obj = await TemplateService.update_template(db, template_id, template)
    if not obj:
        raise HTTPException(status_code=404, detail="Template not found")
    return obj

@router.delete("/{template_id}")
async def delete_template(template_id: str, db: AsyncSession = Depends(get_db())):
    ok = await TemplateService.delete_template(db, template_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Template not found")
    return {"ok": True} 