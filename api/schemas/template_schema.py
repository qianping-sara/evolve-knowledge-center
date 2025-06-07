from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class TemplateBase(BaseModel):
    name: str
    description: str
    content: str
    tags: List[str]
    version: str
    createdBy: str

class TemplateCreate(TemplateBase):
    pass

class TemplateRead(TemplateBase):
    id: str
    createdAt: datetime
    updatedAt: datetime
    
    class Config:
        from_attributes = True  # 允许从ORM模型创建 