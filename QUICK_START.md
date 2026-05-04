# 知奥知识库 - 快速参考

## 日常工作流（3 步）

### 1️⃣ 复制文章
```
复制公众号文章 → 粘贴到 raw/articles/ 文件夹
例如：raw/articles/2026年4月总结.md
```

### 2️⃣ 推送到 GitHub
```bash
cd D:\桌面\AI文件\知奥公众号文章\知奥知识库

git add raw/articles/
git commit -m "新增文章：2026年4月总结"
git push
```

### 3️⃣ 部署到 Fly.io
```bash
# 等待 GitHub Actions 完成（2-3 分钟）
# 然后运行：
flyctl deploy -a zhiao-wiki
```

---

## 监控工作流

### 查看 GitHub Actions 进度
- 进入：https://github.com/sinobiology/zhiao-wiki/actions
- 查看最新的工作流运行

### 查看 Fly.io 部署
```bash
# 查看实时日志
flyctl logs -a zhiao-wiki --follow

# 查看部署状态
flyctl status -a zhiao-wiki
```

---

## 常用命令

```bash
# 查看 Git 状态
git status

# 查看最近提交
git log --oneline -5

# 撤销最后一次提交（未推送）
git reset --soft HEAD~1

# 查看 Fly.io 应用信息
flyctl info -a zhiao-wiki

# 重启应用
flyctl restart -a zhiao-wiki
```

---

## 文件位置

| 位置 | 说明 |
|------|------|
| `raw/articles/` | 你复制粘贴文章的地方 |
| `wiki/summaries/` | 自动生成的摘要 |
| `code/web/public/data/` | 前端使用的 JSON 数据 |
| `.github/workflows/` | GitHub Actions 工作流 |

---

## 成本

- **GitHub**: 免费
- **GitHub Actions**: 免费（每月 2000 分钟）
- **Fly.io**: 按使用量计费（通常 $5-20/月）
- **Anthropic API**: 按 token 计费

---

## 支持

- 仓库：https://github.com/sinobiology/zhiao-wiki
- Fly.io 应用：https://zhiao-wiki.fly.dev
- 问题排查：查看 GitHub Actions 日志或 Fly.io 日志
