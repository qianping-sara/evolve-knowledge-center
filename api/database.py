from dotenv import load_dotenv
import os
import logging
import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# 配置日志
logger = logging.getLogger(__name__)

# 创建基类
Base = declarative_base()

def get_database_url():
    # 确保使用绝对路径创建SQLite数据库文件
    base_dir = pathlib.Path(__file__).parent.parent.absolute()
    db_path = os.path.join(base_dir, "app.db")
    logger.info(f"数据库路径: {db_path}")
    return f"sqlite:///{db_path}"

load_dotenv()
DATABASE_URL = get_database_url()
logger.info(f"使用数据库URL: {DATABASE_URL}")

# 创建同步引擎
engine = create_engine(
    DATABASE_URL, 
    echo=True,
    connect_args={"check_same_thread": False}  # 仅用于SQLite
)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建数据库依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"数据库会话异常: {str(e)}", exc_info=True)
        db.rollback()
        raise
    finally:
        db.close()

def init_db():
    """初始化数据库，创建所有表"""
    try:
        # 创建所有表
        Base.metadata.create_all(bind=engine)
        logger.info("数据库表创建成功")
    except Exception as e:
        logger.error(f"数据库初始化失败: {str(e)}", exc_info=True)
        raise 