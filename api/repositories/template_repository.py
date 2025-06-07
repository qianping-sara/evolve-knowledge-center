from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from api.models.template_model import Template
import json
import logging

# 配置日志
logger = logging.getLogger(__name__)

class TemplateRepository:
    @staticmethod
    def create(db: Session, obj: Template):
        try:
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return TemplateRepository._process_tags(obj)
        except Exception as e:
            logger.error(f"创建模板失败: {str(e)}", exc_info=True)
            db.rollback()
            raise

    @staticmethod
    def get(db: Session, template_id: str):
        try:
            obj = db.query(Template).filter(Template.id == template_id).first()
            if obj:
                return TemplateRepository._process_tags(obj)
            return None
        except Exception as e:
            logger.error(f"获取模板失败: {str(e)}", exc_info=True)
            raise

    @staticmethod
    def list(db: Session):
        try:
            objs = db.query(Template).all()
            return [TemplateRepository._process_tags(obj) for obj in objs]
        except Exception as e:
            logger.error(f"获取模板列表失败: {str(e)}", exc_info=True)
            raise
            
    @staticmethod
    def search(db: Session, keyword: str, skip: int = 0, limit: int = 10):
        """
        根据关键词搜索模板
        
        Args:
            db: 数据库会话
            keyword: 搜索关键词
            skip: 跳过的结果数量（用于分页）
            limit: 返回的最大结果数量（用于分页）
            
        Returns:
            匹配的模板列表和总数
        """
        try:
            # 构建LIKE模式匹配
            pattern = f"%{keyword}%"
            
            # 查询匹配的记录
            query = db.query(Template).filter(
                or_(
                    Template.name.ilike(pattern),       # 模糊匹配name
                    Template.description.ilike(pattern),# 模糊匹配description
                    Template.tags.ilike(pattern)        # 模糊匹配tags（注意这是JSON字符串）
                )
            )
            
            # 获取总数（用于分页信息）
            total = query.count()
            
            # 应用分页
            results = query.offset(skip).limit(limit).all()
            
            # 处理结果
            processed_results = [TemplateRepository._process_tags(obj) for obj in results]
            
            return processed_results, total
        except Exception as e:
            logger.error(f"搜索模板失败: {str(e)}", exc_info=True)
            raise

    @staticmethod
    def update(db: Session, obj: Template):
        try:
            db.commit()
            db.refresh(obj)
            return TemplateRepository._process_tags(obj)
        except Exception as e:
            logger.error(f"更新模板失败: {str(e)}", exc_info=True)
            db.rollback()
            raise

    @staticmethod
    def delete(db: Session, obj: Template):
        try:
            db.delete(obj)
            db.commit()
        except Exception as e:
            logger.error(f"删除模板失败: {str(e)}", exc_info=True)
            db.rollback()
            raise
        
    @staticmethod
    def _process_tags(obj):
        """将JSON字符串格式的tags转换回Python列表"""
        if hasattr(obj, 'tags') and obj.tags:
            if isinstance(obj.tags, str):
                try:
                    obj.tags = json.loads(obj.tags)
                except (json.JSONDecodeError, TypeError) as e:
                    logger.warning(f"解析tags字段失败: {str(e)}，值: {obj.tags}")
                    obj.tags = []
        return obj 