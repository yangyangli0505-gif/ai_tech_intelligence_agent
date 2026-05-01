# Build Plan

这个 build plan 不是“从零造一个新的 agent runtime”，而是：

> **围绕一个 AI 行业 intelligence 场景，先把上层 pipeline 做对，再把它挂到 nanobot / OpenClaw 这类长期运行 runtime 上。**

---

## Phase 0：先定边界

在真正开工前，先明确项目边界：

- 不做通用聊天助手
- 不重造 memory / cron / delivery / tool runtime
- 不先追求“像聊天机器人一样聪明”
- 优先做“持续行业信号识别”这件事

这一步决定了项目核心不是 prompt，而是 pipeline。

---

## Phase 1：先把 intelligence pipeline 跑通

### Step 1：Source Registry
建立首批固定信息源：
- OpenAI Blog
- Google / Gemini 相关博客
- Hugging Face Blog
- 后续再扩展其他高信噪比源

### Step 2：Ingestion + Normalize
把抓到的信息统一成事件结构：
- title
- summary
- url
- source
- published_at
- topics
- metadata

### Step 3：Dedup
先做同源去重，再做跨源粗去重，避免同一条内容反复上榜。

### Step 4：Topic Classification
先做规则版分类，把最常见信号类型分出来。

### Step 5：Signal Ranking
做启发式打分，输出：
- 必须知道
- 值得关注
- 背景补充
- 待观察

### Step 6：Report Generation
先能稳定产出：
- 日报 preview
- 午后复盘 preview

---

## Phase 2：从摘要器变成变化跟踪器

如果系统只会每天重新总结一遍，那它只是一个 summary bot。

所以第二阶段重点是：

### Step 7：Snapshot Diff
加入：
- latest snapshot
- added / repeated / escalated

让系统开始回答：
- 今天新增了什么
- 哪些只是重复延续
- 哪些主题在升温

### Step 8：Change Summary in Brief
把变化摘要放进报告里，而不只是静态排名。

---

## Phase 3：让输出更像 intelligence brief

这一阶段重点不在加源，而在输出质量。

### Step 9：Top Items + Summary
增加：
- 一句话总结
- 今日最重要 3 条
- 分层简报

### Step 10：Why it matters
为每条内容增加：
- 为什么值得看
- 洞察
- 后续关注

这一阶段开始让系统从“会排榜”走向“会解释”。

---

## Phase 4：误判收敛

这是当前最核心的一轮迭代。

### Step 11：压教程 / enablement / case study / roundup
显式识别并降权：
- tutorial_enablement
- case_study
- roundup_recap

目标不是删掉，而是把它们从头条层压回背景层。

### Step 12：保住结构变化型说明文
避免把真正重要的结构性内容误杀，比如：
- orchestration spec
- inference tiers
- managed agents + AWS
- compute infrastructure

### Step 13：单列政策 / 安全叙事
把 policy / security / regulation / trust 相关内容，从“杂音”里分离出来。

### Step 14：细分开源技术内容
针对 Hugging Face 这类技术文章，细分出：
- capability_jump
- eval_infra
- tooling_ecosystem
- paper_style_explainer

### Step 15：加入 source-aware 约束
避免一个来源的语言模式污染另一个来源的分类结果。

---

## Phase 5：typed reasoning

这一阶段开始让“为什么值得看”从 topic 罗列升级成类型化判断。

例如区分：
- 能力边界前移信号
- 评测/验证基础设施成熟信号
- 平台分层/接口重构信号
- 治理/采购口径变化信号
- 工具链成熟度提升信号

这一步的意义是：

> 系统不只是知道“它属于什么类”，还开始知道“它为什么重要”。

---

## Phase 6：可选 LLM 增强

在核心 heuristics 稳定后，再挂可选的 LLM enrich：

- enrich 用于补充洞察表达
- enrich 失败不阻塞主流程
- 主排序逻辑仍由 pipeline 自己控制

这是“heuristics first, LLM optional”的策略。

---

## Phase 7：runtime 集成

等 intelligence pipeline 收敛得更稳后，再更正式地接到 runtime 上：

- cron 定时
- delivery / messaging
- user preferences
- topic/company tracking
- weekly digest / alerts

这里的思路是：

> runtime 负责长期运行与交付，本项目负责 intelligence 理解与产出。

---

## 当前里程碑判断

### M1：已完成
能抓固定源并输出结构化事件

### M2：已完成
能自动生成日报 / 午报预览

### M3：已完成
能判断“新增变化”而不是重复摘要

### M4：部分完成
已经有 runtime 定时推送雏形，但还未完全产品化

### M5：当前重点
继续观察真实输出，修掉剩余误判，让结果更稳
