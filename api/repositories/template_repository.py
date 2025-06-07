from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.template_model import Template
import json

class TemplateRepository:
    @staticmethod
    async def create(db: AsyncSession, obj: Template):
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return TemplateRepository._process_tags(obj)

    @staticmethod
    async def get(db: AsyncSession, template_id: str):
        result = await db.execute(select(Template).where(Template.id == template_id))
        obj = result.scalar_one_or_none()
        if obj:
            return TemplateRepository._process_tags(obj)
        return None

    @staticmethod
    async def list(db: AsyncSession):
        result = await db.execute(select(Template))
        objs = result.scalars().all()
        return [TemplateRepository._process_tags(obj) for obj in objs]

    @staticmethod
    async def update(db: AsyncSession, obj: Template):
        await db.commit()
        await db.refresh(obj)
        return TemplateRepository._process_tags(obj)

    @staticmethod
    async def delete(db: AsyncSession, obj: Template):
        await db.delete(obj)
        await db.commit()
        
    @staticmethod
    def _process_tags(obj):
        """将JSON字符串格式的tags转换回Python列表"""
        if hasattr(obj, 'tags') and obj.tags and isinstance(obj.tags, str):
            try:
                obj.tags = json.loads(obj.tags)
            except (json.JSONDecodeError, TypeError):
                obj.tags = []
        return obj 