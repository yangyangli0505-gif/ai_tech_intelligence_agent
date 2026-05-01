# Resume Positioning

## 项目一句话

一个面向 AI / LLM / Agent 领域的垂直 intelligence pipeline，设计上运行在长期运行 agent runtime（如 nanobot / OpenClaw）之上，持续监控多源信息、识别高价值变化，并主动生成日报、复盘与变化摘要。

---

## 更准确的讲法

如果对外表达，建议不要直接说成“我改了 nanobot 内核”。  
更准确的说法是：

> 我围绕 nanobot / OpenClaw 这类长期运行 agent runtime 的能力边界，开发了一个上层的 AI 技术情报应用。runtime 负责定时、推送、记忆和长期运行；我重点做的是多源抓取、分类、排序、变化检测和类型化解释。

这样说更真实，也更不容易被追问卡住。

---

## 简历亮点拆解

### 工程能力
- 多源信息抓取与统一事件建模
- 去重、变化检测、主题分类、信号排序
- 规则系统 + optional LLM enhancement
- source-aware 规则设计与误判收敛

### 产品/分析能力
- 面向 AI / LLM / Agent 行业的垂直 intelligence 场景
- 将资讯流转化为“主信号 / 辅助内容 / 背景噪音”的分层判断
- 为每条内容生成 typed reasoning、洞察和后续关注点

### Agent / Runtime 结合能力
- 基于长期运行 runtime 的 cron + 主动推送 workflow
- 利用 runtime 处理 delivery、memory、调度
- 上层只专注 intelligence pipeline，而不是重造通用 agent 壳层

---

## 面试讲法关键词

- intelligence pipeline
- multi-source monitoring
- change detection
- signal ranking
- typed reasoning
- source-aware classification
- proactive delivery
- long-running agent runtime

---

## 和 myagent-new-v3 的互补关系

### myagent-new-v3
- 更像从零搭 agent harness 原型
- 强调权限、工具、RAG、MCP、compression、agent loop

### AI Tech Intelligence Agent
- 更像基于已有 runtime 思路做场景化上层应用
- 强调长期运行、情报分析、主动交付、误判收敛、typed reasoning

两者互补在于：

- 前者偏“agent 基础设施 / harness 理解”
- 后者偏“面向垂直场景的 intelligence 产品化”
