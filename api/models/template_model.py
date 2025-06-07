from sqlalchemy import Column, String, DateTime, ARRAY, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Template(Base):
    __tablename__ = 'template'
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    content = Column(Text)
    tags = Column(ARRAY(String))
    version = Column(String)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    createdBy = Column(String, index=True) 