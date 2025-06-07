from sqlalchemy import Column, String, DateTime, Text, event
from datetime import datetime
import json
import time
from api.database import Base

class Template(Base):
    __tablename__ = 'template'
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    content = Column(Text)
    tags = Column(Text)  # 存储为JSON字符串
    version = Column(String)  # 版本号将自动基于时间戳生成
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    createdBy = Column(String, index=True)
    
    def __init__(self, **kwargs):
        # 处理tags字段
        if 'tags' in kwargs and isinstance(kwargs['tags'], list):
            kwargs['tags'] = json.dumps(kwargs['tags'])
        
        # 如果没有提供version，则自动生成基于时间戳的版本号
        if 'version' not in kwargs or not kwargs['version']:
            kwargs['version'] = f"v{int(time.time())}"
            
        super().__init__(**kwargs)

# 添加事件监听器，在对象更新时自动更新版本号
@event.listens_for(Template, 'before_update')
def before_update(mapper, connection, target):
    # 更新版本号为当前时间戳
    target.version = f"v{int(time.time())}" 