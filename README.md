# FastAPI Template API 项目

## 简介
本项目基于 FastAPI + SQLAlchemy + PostgreSQL，支持异步ORM，自动生成Swagger文档，并集成 fastapi_mcp。

## 主要特性
- FastAPI 框架，自动生成Swagger文档
- PostgreSQL 数据库，异步ORM（SQLAlchemy）
- 支持Vercel Serverless部署
- 集成 fastapi_mcp

## 快速开始

### 1. 安装依赖\本地运行
```bash
python3.12 -m venv .venv
pip install -r requirements.txt
uvicorn api.main:app --reload
```

### 2. 配置数据库
请设置环境变量 `DATABASE_URL`，例如：
```
export DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
alembic stamp head
alembic revision --autogenerate -m "Add template table"
alembic upgrade head
```

### 3. 访问API文档
- Swagger: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

### 4. Vercel 部署
- 需确保 `vercel.json` 配置正确，入口为 `api/main.py`
- 支持 requirements.txt 自动安装依赖
- 参考官方文档: https://vercel.com/docs/functions/runtimes/python

## API接口

- `GET /templates`: 获取所有模板
- `GET /templates/{id}`: 获取单个模板
- `POST /templates`: 创建新模板
- `PUT /templates/{id}`: 更新模板
- `DELETE /templates/{id}`: 删除模板
- `GET /health`: 健康检查

## 参考
- [Vercel Python Runtime 文档](https://vercel.com/docs/functions/runtimes/python)
- [fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)
