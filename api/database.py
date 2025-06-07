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
    # 首先检查环境变量中是否有DATABASE_URL
    db_url = os.getenv("DATABASE_URL")
    if db_url:
        # 如果URL以postgres://开头，转换为postgresql://
        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://", 1)
        logger.info(f"使用环境变量中的数据库URL")
        return db_url
    
    # 如果环境变量中没有，则使用SQLite作为备选
    base_dir = pathlib.Path(__file__).parent.parent.absolute()
    db_path = os.path.join(base_dir, "app.db")
    logger.info(f"未找到环境变量中的数据库URL，使用SQLite: {db_path}")
    return f"sqlite:///{db_path}"

# 加载环境变量
load_dotenv()
DATABASE_URL = get_database_url()
logger.info(f"最终使用的数据库URL: {DATABASE_URL}")

# 根据数据库类型设置不同的连接参数
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args["check_same_thread"] = False

# 创建同步引擎
engine = create_engine(
    DATABASE_URL, 
    echo=True,
    connect_args=connect_args
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