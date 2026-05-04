---
title: "（可能全网最全/长的）2万字Openclaw保姆教程"
type: "技术"
tags: ["AI Agent", "OpenClaw", "飞书集成", "新手教程", "本地部署"]
source_articles: ["（可能全网最全_长的）2万字Openclaw保姆教程.md"]
created: "2026-05-01"
entities: ["OpenClaw", "飞书", "Telegram", "ChatGPT", "Claude", "KIMI", "MiniMax", "GLM", "OpenRouter", "Anthropic", "GPT-5.3-Codex", "Claude Opus 4.6", "Claude Sonnet 4.6", "KIMI K2.5", "OpenAI"]
---

# （可能全网最全/长的）2万字Openclaw保姆教程

## 核心逻辑
- OpenClaw 是一个本地运行的 AI 智能体平台（Agent Platform），核心价值在于让普通用户在自己电脑上搭建 AI 助理并接入飞书等日常工具，数据不经第三方服务器。
- 2026年 AI Agent 从"玩具"变"工具"的临界点已到：大模型指令理解能力质变 + 工程化框架成熟 + 真实场景下省时收益超过学习成本。
- 平台设计遵循最小权限原则，默认无任何权限，所有高风险操作需明确授权或二次确认，安全性是核心卖点。

## 行业洞察
- AI Agent 赛道在 2025-2026 年迎来爆发，驱动力是模型能力（稳定输出格式、理解复杂指令）与工程化工具（消息路由、工具调用框架、权限管理）的双重成熟。
- 本地部署型 Agent 平台对数据隐私敏感的企业和个人有巨大吸引力，是与纯云端 AI 产品的差异化竞争点。
- Agent 平台不是模型的竞争者，而是模型的使用者——可同时接入 OpenAI、Claude、KIMI、MiniMax 等多家模型 API，形成"模型中立"的生态位。

## 技术/管理要点
- **核心架构五要素**：Agent（智能体，自主执行任务）、Gateway（网关，消息路由调度，默认 `127.0.0.1:18789`）、Channel（渠道，接入飞书/Telegram 等）、Tool（工具，具体功能如读写文件、搜索网页）、Skill（技能，定义何时用何工具的说明书）
- **入门三要素**：一台能上网的电脑（Win/Mac/Linux）、一个 API Key、10 分钟时间
- **三条阅读路径设计**：
  - 路径 A（快速用起来）：了解概念 → 准备 API Key → 安装 → 接入飞书 → 安全配置，约 2-3 小时
  - 路径 B（深度定制）：路径 A + Tools/Skills 学习与编写，约 1-2 天
  - 路径 C（服务器部署）：路径 A + 模型配置优化 + 安全沙箱 + 多 Workspace + 运维，约 2-3 天
- **安全设计原则**：最小权限、沙箱执行、二次确认机制；本地运行但调用模型时仍需联网，消息会发送至对应 AI 服务商
- **国内 API Key 方案**：KIMI / MiniMax / GLM 的 Coding Plan，备选 OpenRouter / Anthropic

## 关联实体
[[OpenClaw]] · [[AI Agent]] · [[飞书]] · [[Telegram]] · [[ChatGPT]] · [[Claude]] · [[KIMI]] · [[MiniMax]] · [[GLM]] · [[OpenRouter]] · [[Anthropic]] · [[OpenAI]] · [[GPT-5.3-Codex]] · [[Claude Opus 4.6]] · [[Claude Sonnet 4.6]] · [[KIMI K2.5]] · [[Gateway]] · [[最小权限原则]] · [[API Key]] · [[规模效应]]

## 金句归纳
> "OpenClaw就是这个实习生，只不过它住在你的电脑里。"

> "当省下的时间超过学习成本时，普及就水到渠成了。"