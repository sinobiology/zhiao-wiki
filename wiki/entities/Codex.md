---
title: "Codex"
type: "产品"
tags: ["AI Agent", "OpenAI", "开发工具"]
created: "2026-10-12"
entities: ["OpenAI", "Claude Code", "AI Agent", "Superpowers", "ChatGPT"]
---

# Codex

## 定义
Codex 是 OpenAI 推出的 AI Agent 工具，可在用户电脑上实际执行任务，如文件操作、环境部署、代码编写与数据迁移。它定位为能「坐到电脑前陪用户把路走完」的智能体，区别于只提供路线图的普通问答型 AI。

## 在知奥体系中的位置
在知奥体系中，Codex 是 [[AI Agent]] 实践生态中的一个关键产品节点，与 [[Claude Code]]、[[Cursor]] 等工具并列为当前主流 Agent 执行环境。知奥文章多次将其作为讨论 AI 权限边界、工作流建设和设备生态迁移的切入点——例如《2026年6月总结》在讨论 AI Agent 权限边界时将其与 [[AI Agent]] 一并提及，说明它代表 AI 从「回答问题」走向「真实执行」的阶段。

Codex 也与 [[Superpowers]] 存在兼容关系，后者作为流程层插件适配 Codex，为 Agent 引入规划、拆解、执行、审查、复盘的结构化工作流。此外，Codex 的导入能力与 [[Claude Code]] 形成用户迁移竞争，体现工具厂商之间的生态争夺。在设备生态上，Codex 与 [[ChatGPT]] 客户端体验共同影响用户对 macOS 与 iPhone 等平台的选择。

## 关键数据
- 教程转载自「数字生命卡兹克」，日期为 2026-06-02。
- 几个月内 Codex 进入「爆更模式」，被作者形容为「几乎是两个产品了」。
- 作者用的 ChatGPT 会员额度为 100 美刀/月，另有 200 美刀用于 Claude；轻度使用 20 美刀/月勉强可用，也可用 API key。
- 支持从 Claude Code 和 Cowork 直接导入所有内容、一键继承配置。
- 安装前提：需要魔法和 ChatGPT 账号，从 OpenAI Codex 官网下载，支持 Mac 和 Windows。
- 权限分三档：默认权限（操作需审批）、自动审查（拦截高风险操作）、完全访问权限（不再逐次征求意见）。
- 项目功能以本地文件夹为工作区间，一个项目可开多个对话，每条对话独立任务线但共享同一文件夹文件。
- AGENTS.md 被描述为「从上往下分层穿透的约束体系」，相当于用户给 Codex 设置的「家法」。
- 在小米笔记迁移项目中，Codex 找到开源工具 nogiszd/xiaomi-note-exporter；部署过程中检测到本机无 Rust，随后完成从源码构建、安装依赖、构建 Tauri 应用到安装运行的全流程，最终 55 个 Rust 测试全部通过。
- 该迁移项目处理量为 590 条小米笔记。

## 关联实体
- [[Claude Code]]
- [[AI Agent]]
- [[Superpowers]]
- [[ChatGPT]]
- [[Cursor]]
- [[OpenCode]]
- [[OpenAI]]
- [[小米]]

## 相关文章
[[2026年6月总结]]
[[从0到1带你速通Codex_我整理的终极保姆教程来了_]]
[[从小米到苹果_我用_Codex_把_590_条小米笔记迁移到_iPhone_备忘录]]
[[安利一个11万Star的必装插件_能让你的Agent体验直接质变_]]
