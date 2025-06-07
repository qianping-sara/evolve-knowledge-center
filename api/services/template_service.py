import uuid
from api.models.template_model import Template
from api.schemas.template_schema import TemplateCreate
from api.repositories.template_repository import TemplateRepository
from typing import Tuple, List, Optional

class TemplateService:
    @staticmethod
    def create_template(db, data: TemplateCreate):
        # 将Pydantic模型转换为字典，并确保tags列表被正确处理
        data_dict = data.dict()
        
        # 创建新的Template实例
        obj = Template(
            id=str(uuid.uuid4()),
            **data_dict
        )
        
        return TemplateRepository.create(db, obj)

    @staticmethod
    def get_template(db, template_id: str):
        return TemplateRepository.get(db, template_id)

    @staticmethod
    def list_templates(db):
        return TemplateRepository.list(db)
        
    @staticmethod
    def search_templates(db, keyword: str, skip: int = 0, limit: int = 10) -> Tuple[List[Template], int]:
        """
        搜索模板
        
        Args:
            db: 数据库会话
            keyword: 搜索关键词
            skip: 跳过的结果数量（用于分页）
            limit: 返回的最大结果数量（用于分页）
            
        Returns:
            Tuple[List[Template], int]: 匹配的模板列表和总数
        """
        return TemplateRepository.search(db, keyword, skip, limit)

    @staticmethod
    def update_template(db, template_id: str, data: TemplateCreate):
        obj = TemplateRepository.get(db, template_id)
        if not obj:
            return None
            
        # 将Pydantic模型转换为字典
        data_dict = data.dict()
        
        # 更新属性
        for k, v in data_dict.items():
            setattr(obj, k, v)
            
        return TemplateRepository.update(db, obj)

    @staticmethod
    def delete_template(db, template_id: str):
        obj = TemplateRepository.get(db, template_id)
        if not obj:
            return None
        TemplateRepository.delete(db, obj)
        return True 