from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from api.schemas.template_schema import TemplateCreate, TemplateRead, TemplatePagination
from api.services.template_service import TemplateService
from api.database import get_db
from typing import List, Optional
import logging

# 配置日志
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/templates", tags=["Template"])

@router.post("/", response_model=TemplateRead, operation_id="create_template")
def create_template(template: TemplateCreate, db: Session = Depends(get_db)):
    try:
        result = TemplateService.create_template(db, template)
        return result
    except Exception as e:
        logger.error(f"创建模板失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"创建模板失败: {str(e)}")

@router.get("/", response_model=List[TemplateRead], operation_id="list_templates")
def list_templates(db: Session = Depends(get_db)):
    try:
        return TemplateService.list_templates(db)
    except Exception as e:
        logger.error(f"获取模板列表失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"获取模板列表失败: {str(e)}")

@router.get("/search", response_model=TemplatePagination, operation_id="search_templates")
def search_templates(
    keyword: str = Query(..., description="搜索关键词"),
    skip: int = Query(0, description="跳过的结果数量", ge=0),
    limit: int = Query(20, description="返回的最大结果数量", ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    搜索模板
    
    根据关键词搜索模板，支持对名称、描述和标签进行模糊匹配
    """
    try:
        templates, total = TemplateService.search_templates(db, keyword, skip, limit)
        return {
            "items": templates,
            "total": total,
            "limit": limit,
            "skip": skip,
            "keyword": keyword
        }
    except Exception as e:
        logger.error(f"搜索模板失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"搜索模板失败: {str(e)}")

@router.get("/{template_id}", response_model=TemplateRead, operation_id="get_template_by_id")
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

@router.put("/{template_id}", response_model=TemplateRead, operation_id="update_template")
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

@router.delete("/{template_id}", operation_id="delete_template")
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