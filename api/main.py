import os
import logging
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from api.models.template_model import Template
from api.routers.template_router import router as template_router
from api.database import init_db

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Template API", description="API for Template model", version="0.1.0")

# 添加路由 - 添加v1前缀
app.include_router(template_router, prefix="/v1")

# 添加MCP服务器，自动封装模板相关接口
template_mcp = FastApiMCP(
    app,    
    name="Template MCP",
    include_operations=["create_template", "search_templates", "list_templates"]
)
# 修改为/api路径下的挂载点
template_mcp.mount(mount_path="template")

@app.on_event("startup")
def startup():
    logger.info("应用程序启动中...")
    try:
        # 初始化数据库
        init_db()
        logger.info("数据库初始化完成")
    except Exception as e:
        logger.error(f"启动失败: {str(e)}", exc_info=True)

@app.get("/health",operation_id="health")
async def health():
    return {"status": "ok"} 