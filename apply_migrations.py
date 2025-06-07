import sys
import os
from alembic.config import Config
from alembic import command

# 确保导入路径正确
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def apply_migrations():
    """应用所有待执行的迁移"""
    # 创建Alembic配置
    alembic_cfg = Config("alembic.ini")
    
    # 应用迁移
    print("正在应用数据库迁移...")
    command.upgrade(alembic_cfg, "head")
    print("迁移应用完成!")

if __name__ == "__main__":
    apply_migrations() 