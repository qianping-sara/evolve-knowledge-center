from pydantic import BaseModel
from typing import List
from datetime import datetime

class TemplateCreate(BaseModel):
    name: str
    description: str
    content: str
    tags: List[str]
    version: str
    createdBy: str

class TemplateRead(TemplateCreate):
    id: str
    createdAt: datetime
    updatedAt: datetime 