# Architecture

## 项目定位

这个项目的准确定位是：

> **一个面向 AI / LLM / Agent 领域的垂直 intelligence pipeline，设计上适合运行在 nanobot / OpenClaw 这类长期运行 agent runtime 之上。**

它不是要重造 runtime，也不是当前直接修改 nanobot 内核代码的 fork。  
它负责的是“情报理解层”，而不是“通用 agent 壳层”。

---

## 分层关系

```text
[nanobot / OpenClaw runtime]
  ├─ cron / scheduling
  ├─ delivery / messaging
  ├─ session / memory
  ├─ long-running process model
  └─ user preferences / interaction

[AI Tech Intelligence Agent]
  ├─ source registry
  ├─ ingestion / normalization
  ├─ dedup
  ├─ topic classification
  ├─ signal ranking
  ├─ typed reasoning
  ├─ change detection
  └─ brief generation
```

也就是说：

- **runtime 负责长期运行能力**
- **本项目负责 AI 行业信息的理解、分层、解释和输出**

---

## 当前核心流程

```text
[Source Registry]
   ├─ OpenAI Blog
   ├─ Google Blog / Gemini
   ├─ Hugging Face Blog
   └─ More sources later
          |
          v
[Ingestion]
   fetch -> parse -> normalize
          |
          v
[Unified Events]
   {title, summary, source, url, published_at, topics, metadata}
          |
     +----+----+
     |         |
     v         v
 [Dedup]   [Topic Classifier]
     |         |
     +----+----+
          |
          v
   [Signal Ranker]
          |
          +--> signal bucket
          +--> reason
          +--> heuristic insight
          +--> watch next
          |
          v
 [Change Detection / Snapshot Diff]
          |
          v
 [Report Generator]
   ├─ 08:00 日报
   ├─ 15:00 午后复盘
   └─ 变化摘要 / 分层简报
          |
          v
 [Optional LLM Enrichment]
          |
          v
 [Runtime Delivery]
   via nanobot / OpenClaw cron + messaging
```

---

## 三层架构解释

### 1. 信息处理层
负责“把东西收上来”。

包括：
- source registry
- ingestion
- normalization
- dedup

这一层解决的是：
- 信息源怎么管理
- 抓到的内容怎么变成统一事件
- 同一件事怎么避免重复

---

### 2. 情报理解层
负责“判断什么值得看”。

包括：
- topic classification
- signal ranking
- typed reasoning
- change detection
- heuristic insight
- watch next

这一层解决的是：
- 什么是主信号，什么是辅助内容
- 这条为什么重要
- 它影响的是能力边界、平台结构、治理预期，还是工具链生态
- 相比上一轮，新增了什么、哪些在升温

---

### 3. runtime 集成层
负责“把结果稳定交付出去”。

包括：
- cron scheduling
- delivery / messaging
- session / memory
- user preferences
- proactive push

这一层解决的是：
- 什么时候跑
- 跑完发给谁
- 用户关注什么主题
- 怎样形成持续追踪而不是单次生成

---

## 当前实现状态

当前项目已经基本成型的是：

### 已实现
- source registry
- RSS ingestion
- normalized event model
- dedup
- topic classification
- signal ranking
- typed reasoning
- heuristic insight
- watch next
- snapshot diff
- brief preview generation
- optional LLM enrichment

### 已有雏形但还不算完全产品化
- 定时生成日报/午报
- 与 runtime 的稳定集成
- 更正式的主题订阅 / company tracking
- 更成熟的 delivery 展示层

---

## 当前策略

当前最合理的路线不是先去改 nanobot 内核，而是：

1. 先把 intelligence pipeline 自己收敛清楚
2. 再把它以更稳定的方式挂到 runtime 上
3. 最后再决定是否做成更明确的 plugin / skill / app 形态

所以这个项目目前更准确的说法是：

> **面向 nanobot / OpenClaw runtime 的垂直 intelligence 应用层。**
