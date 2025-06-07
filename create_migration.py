import os
import sys
from alembic.config import Config
from alembic import command

# 确保导入路径正确
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def create_migration(message):
    """
    创建一个新的迁移脚本
    
    Args:
        message: 迁移消息描述
    """
    # 创建Alembic配置
    alembic_cfg = Config("alembic.ini")
    
    # 自动生成迁移脚本
    print(f"正在创建迁移脚本: {message}")
    command.revision(alembic_cfg, message=message, autogenerate=True)
    print("迁移脚本创建完成!")

if __name__ == "__main__":
    # 获取命令行参数
    if len(sys.argv) < 2:
        print("使用方法: python create_migration.py '迁移描述'")
        sys.exit(1)
    
    message = sys.argv[1]
    create_migration(message) 