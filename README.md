# AI Tech Intelligence Agent

一个基于 nanobot / OpenClaw 这类长期运行 Agent runtime 的二次开发项目，目标不是“做一个新闻摘要机器人”，而是做一个 **面向 AI / LLM / Agent 领域的持续情报跟踪助手**。

## 项目目标

帮助用户从分散的信息源中，持续识别高价值技术信号，而不是被动接收海量资讯。

核心能力：

1. **多源监控**：RSS、官方博客、GitHub Releases、公开媒体
2. **主题追踪**：模型升级、Agent、MCP、开源模型、infra、eval、安全等
3. **变化检测**：和昨天/上周相比，新增了什么，哪些主题在升温
4. **信号分层**：必须知道 / 值得关注 / 背景噪音 / 待观察
5. **主动推送**：日报、午后复盘、专题追踪、异常提醒
6. **时间线积累**：为公司/主题维护持续上下文，而不是一次性总结

---

## 为什么这个项目适合 nanobot 二开

nanobot 擅长的是：

- 长期运行
- cron 定时任务
- session / memory
- 聊天入口与主动推送
- MCP / 工具接入
- runtime 稳定性

这个项目不重造这些底座，而是在其上面开发：

- 信息源管理
- 情报归一化
- 主题分类与追踪
- 变化检测
- 报告生成策略
- 用户偏好与关注列表

---

## MVP 定义（第一阶段）

### 输入源

先只做公开、稳定、低维护的源：

- OpenAI Blog
- Google Blog / DeepMind / Gemini updates
- Hugging Face Blog
- Anthropic News / docs updates（能抓到就接）
- GitHub Releases（指定 repo）
- Reuters / TechCrunch / The Verge（可选）

### 输出形态

1. **08:00 日报**
   - 昨夜到今晨值得知道的 AI / LLM / Agent / infra 动态
2. **15:00 午后复盘**
   - 当日新增变化与值得注意的行业信号
3. **专题追踪卡**
   - 例如 OpenAI / Google / MCP / 开源模型 的近 7 天变化

### MVP 必须做到

- 多源抓取
- 去重
- 基础主题分类
- 基础信号排序
- 与上次结果做 diff
- 输出固定格式简报

### MVP 暂时不做

- 全自动网页浏览器抓取
- 复杂 RAG 知识库
- 多语言扩展
- 高级用户画像
- 可视化 dashboard

---

## 项目定位（一句话）

> 基于长期运行 Agent runtime 的 AI 技术情报跟踪助手，持续监控 AI / LLM / Agent 生态，识别高价值变化，并以日报、复盘和专题追踪形式主动交付。
