# FastAPI Template API 项目

## 简介
本项目基于 FastAPI + SQLAlchemy + PostgreSQL，支持异步ORM，自动生成Swagger文档，并集成 fastapi_mcp。

## 主要特性
- FastAPI 框架，自动生成Swagger文档
- PostgreSQL 数据库，异步ORM（SQLAlchemy）
- 支持Vercel Serverless部署
- 集成 fastapi_mcp

## 快速开始

### 1. 安装依赖
```bash
python3 -m venv venv
pip install -r requirements.txt
```

### 2. 配置数据库
请设置环境变量 `DATABASE_URL`，例如：
```
export DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
```

### 3. 本地运行
```bash
uvicorn api.main:app --reload
```

### 4. 访问API文档
- Swagger: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

### 5. Vercel 部署
- 需确保 `vercel.json` 配置正确，入口为 `api/main.py`
- 支持 requirements.txt 自动安装依赖
- 参考官方文档: https://vercel.com/docs/functions/runtimes/python

## 参考
- [Vercel Python Runtime 文档](https://vercel.com/docs/functions/runtimes/python)
- [fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)

# 知识中心API

基于FastAPI的知识中心后端API服务。

## 功能特性

- 使用FastAPI框架
- SQLAlchemy ORM集成
- 支持SQLite和PostgreSQL数据库
- 完整的CRUD API
- Swagger文档自动生成
- 支持Vercel部署
- MCP工具集成
- Alembic数据库迁移

## 快速开始

### 环境准备

1. 创建虚拟环境并安装依赖

```bash
# 创建Python 3.12虚拟环境
python3.12 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 数据库迁移

项目使用Alembic进行数据库迁移管理。

1. 创建新的迁移脚本

```bash
python create_migration.py "创建模板表"
```

2. 应用迁移

```bash
python apply_migrations.py
```

### 启动应用

```bash
# 开发环境启动
uvicorn api.main:app --reload
```

访问 http://localhost:8000/docs 查看API文档。

## API接口

- `GET /templates`: 获取所有模板
- `GET /templates/{id}`: 获取单个模板
- `POST /templates`: 创建新模板
- `PUT /templates/{id}`: 更新模板
- `DELETE /templates/{id}`: 删除模板
- `GET /health`: 健康检查

## 数据库配置

默认使用SQLite数据库。如果需要使用PostgreSQL，可以设置环境变量：

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
```

## 部署

### Vercel部署

项目包含`vercel.json`配置文件，可以直接部署到Vercel。 