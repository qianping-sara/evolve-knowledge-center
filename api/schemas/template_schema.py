from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class TemplateBase(BaseModel):
    name: str
    description: str
    content: str
    tags: List[str]
    version: Optional[str] = None
    createdBy: Optional[str] = None

class TemplateCreate(TemplateBase):
    pass

class TemplateRead(TemplateBase):
    id: str
    createdAt: datetime
    updatedAt: datetime
    version: str
    createdBy: str
    
    class Config:
        from_attributes = True  # 允许从ORM模型创建 
        
class TemplatePagination(BaseModel):
    """分页搜索结果"""
    items: List[TemplateRead]
    total: int
    limit: int
    skip: int
    keyword: str