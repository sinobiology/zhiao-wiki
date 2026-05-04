@echo off
echo ========================================
echo   知奥ZHAO 知识库 - 启动脚本
echo ========================================
echo.

REM 检查 API Key
if "%ANTHROPIC_API_KEY%"=="" (
  echo [错误] 请先设置 ANTHROPIC_API_KEY 环境变量
  echo   set ANTHROPIC_API_KEY=sk-ant-你的key
  pause
  exit /b 1
)

echo [1/3] 启动后端服务 (端口 3001)...
start "知奥后端" cmd /k "cd /d %~dp0backend && node server.js"

timeout /t 2 /nobreak >nul

echo [2/3] 启动前端开发服务器 (端口 5173)...
start "知奥前端" cmd /k "cd /d %~dp0frontend && npm run dev"

timeout /t 3 /nobreak >nul

echo [3/3] 打开浏览器...
start http://localhost:5173

echo.
echo 知识库已启动！
echo   前端: http://localhost:5173
echo   后端: http://localhost:3001
echo.
echo 如需生成知识库摘要，请运行：
echo   python code\ingest.py --file 文章名.md   (测试单篇)
echo   python code\ingest.py                    (处理全部)
echo.
pause
