from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime
import json

Base = declarative_base()

class Template(Base):
    __tablename__ = 'template'
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    content = Column(Text)
    tags = Column(Text)  # 存储为JSON字符串
    version = Column(String)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    createdBy = Column(String, index=True)
    
    def __init__(self, **kwargs):
        if 'tags' in kwargs and isinstance(kwargs['tags'], list):
            kwargs['tags'] = json.dumps(kwargs['tags'])
        super().__init__(**kwargs) 