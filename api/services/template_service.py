import uuid
from api.models.template_model import Template
from api.schemas.template_schema import TemplateCreate
from api.repositories.template_repository import TemplateRepository

class TemplateService:
    @staticmethod
    async def create_template(db, data: TemplateCreate):
        obj = Template(
            id=str(uuid.uuid4()),
            **data.dict()
        )
        return await TemplateRepository.create(db, obj)

    @staticmethod
    async def get_template(db, template_id: str):
        return await TemplateRepository.get(db, template_id)

    @staticmethod
    async def list_templates(db):
        return await TemplateRepository.list(db)

    @staticmethod
    async def update_template(db, template_id: str, data: TemplateCreate):
        obj = await TemplateRepository.get(db, template_id)
        if not obj:
            return None
        for k, v in data.dict().items():
            setattr(obj, k, v)
        return await TemplateRepository.update(db, obj)

    @staticmethod
    async def delete_template(db, template_id: str):
        obj = await TemplateRepository.get(db, template_id)
        if not obj:
            return None
        await TemplateRepository.delete(db, obj)
        return True 