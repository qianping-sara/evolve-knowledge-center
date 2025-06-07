#!/bin/bash
set -e

# 检测操作系统
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    source venv/bin/activate
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    source venv/bin/activate
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    echo "未知操作系统: $OSTYPE"
    exit 1
fi

# 安装依赖
pip install -r requirements.txt

# 启动应用
echo "正在启动应用..."
uvicorn api.main:app --reload --port 8000

# 如果以上命令执行完毕，提示访问信息
echo "应用已停止" 