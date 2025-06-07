from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.schemas.template_schema import TemplateCreate, TemplateRead
from api.services.template_service import TemplateService
from api.database import get_db
from typing import List
import logging

# 配置日志
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/templates", tags=["Template"])

@router.post("/", response_model=TemplateRead)
def create_template(template: TemplateCreate, db: Session = Depends(get_db)):
    try:
        result = TemplateService.create_template(db, template)
        return result
    except Exception as e:
        logger.error(f"创建模板失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"创建模板失败: {str(e)}")

@router.get("/", response_model=List[TemplateRead])
def list_templates(db: Session = Depends(get_db)):
    try:
        return TemplateService.list_templates(db)
    except Exception as e:
        logger.error(f"获取模板列表失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"获取模板列表失败: {str(e)}")

@router.get("/{template_id}", response_model=TemplateRead)
def get_template(template_id: str, db: Session = Depends(get_db)):
    try:
        obj = TemplateService.get_template(db, template_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Template not found")
        return obj
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"获取模板失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"获取模板失败: {str(e)}")

@router.put("/{template_id}", response_model=TemplateRead)
def update_template(template_id: str, template: TemplateCreate, db: Session = Depends(get_db)):
    try:
        obj = TemplateService.update_template(db, template_id, template)
        if not obj:
            raise HTTPException(status_code=404, detail="Template not found")
        return obj
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"更新模板失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"更新模板失败: {str(e)}")

@router.delete("/{template_id}")
def delete_template(template_id: str, db: Session = Depends(get_db)):
    try:
        ok = TemplateService.delete_template(db, template_id)
        if not ok:
            raise HTTPException(status_code=404, detail="Template not found")
        return {"ok": True}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"删除模板失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"删除模板失败: {str(e)}") 