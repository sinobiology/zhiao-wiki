# 知奥知识库 - 部署指南

## 快速开始

### 1. 初始化 Git 仓库并推送到 GitHub

```bash
cd D:\桌面\AI文件\知奥公众号文章\知奥知识库

# 初始化 Git
git init
git add .
git commit -m "Initial commit: zhiao-wiki knowledge base"
git branch -M main

# 添加远程仓库（替换为你的 GitHub 用户名）
git remote add origin https://github.com/你的用户名/zhiao-wiki.git
git push -u origin main
```

### 2. 配置 GitHub Secrets

在 GitHub 仓库设置中添加 Secret：

1. 进入 GitHub 仓库 → Settings → Secrets and variables → Actions
2. 点击 "New repository secret"
3. 添加以下 Secret：
   - **名称**: `ANTHROPIC_API_KEY`
   - **值**: 你的 Anthropic API Key（从 https://console.anthropic.com 获取）

### 3. 工作流程

#### 添加新文章

```bash
# 1. 复制公众号文章到 raw/articles/ 文件夹
# 例如：raw/articles/新文章标题.md

# 2. 推送到 GitHub
git add raw/articles/
git commit -m "新增文章：新文章标题"
git push

# 3. GitHub Actions 自动运行
# - 运行 ingest.py 生成摘要
# - 运行 build-data.py 生成 JSON 数据
# - 自动提交更新

# 4. 重新部署到 Fly.io
flyctl deploy -a zhiao-wiki
```

#### 手动触发更新（可选）

如果想手动触发 GitHub Actions：
1. 进入 GitHub 仓库 → Actions
2. 选择 "自动更新知识库" 工作流
3. 点击 "Run workflow"

### 4. 监控部署

#### 查看 GitHub Actions 日志
- 进入 GitHub 仓库 → Actions
- 查看最新的工作流运行结果

#### 查看 Fly.io 部署
```bash
# 查看部署状态
flyctl status -a zhiao-wiki

# 查看实时日志
flyctl logs -a zhiao-wiki --follow

# 查看应用信息
flyctl info -a zhiao-wiki
```

## 文件结构

```
zhiao-wiki/
├── raw/articles/           # 原始文章（你复制粘贴的地方）
├── wiki/
│   ├── summaries/          # 自动生成的摘要
│   ├── entities/           # 实体页面
│   ├── SCHEMA.md           # Wiki 规范
│   └── README.md           # Wiki 入口
├── code/
│   ├── ingest.py           # 生成摘要脚本
│   └── web/
│       ├── scripts/build-data.py  # 生成 JSON 脚本
│       ├── server.js       # Express 后端
│       ├── public/data/    # 前端数据（自动生成）
│       └── package.json
├── frontend/               # Vue 前端
├── .github/workflows/      # GitHub Actions 工作流
├── .gitignore             # Git 忽略文件
└── fly.toml               # Fly.io 配置
```

## 常见问题

### Q: GitHub Actions 失败了怎么办？

A: 检查以下几点：
1. 是否配置了 `ANTHROPIC_API_KEY` Secret？
2. 文章格式是否正确（需要 YAML Frontmatter）？
3. 查看 Actions 日志了解具体错误

### Q: 如何手动运行脚本？

A: 在本地运行：
```bash
# 生成摘要
cd code
python ingest.py

# 生成 JSON 数据
cd web/scripts
python build-data.py
```

### Q: 部署到 Fly.io 需要多久？

A: 通常 2-5 分钟。可以用 `flyctl logs -a zhiao-wiki --follow` 监控。

### Q: 如何回滚到之前的版本？

A: 
```bash
# 查看提交历史
git log

# 回滚到某个提交
git revert <commit-hash>
git push

# 重新部署
flyctl deploy -a zhiao-wiki
```

## 成本估算

- **GitHub**: 免费（公开仓库）
- **GitHub Actions**: 免费（每月 2000 分钟）
- **Fly.io**: 按使用量计费（通常 $5-20/月）
- **Anthropic API**: 按 token 计费（取决于文章数量）

## 支持

- Fly.io 文档: https://fly.io/docs/
- GitHub Actions 文档: https://docs.github.com/en/actions
- Anthropic API 文档: https://docs.anthropic.com/
