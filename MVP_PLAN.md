# MVP Plan

## 一、产品边界

这个项目不是：
- 通用聊天助手
- 通用个人助理
- 单纯新闻摘要器
- nanobot 内核重写项目

它当前更准确的定位是：

> **一个面向 AI / LLM / Agent 领域的持续情报跟踪系统，设计上适合运行在 nanobot / OpenClaw 这类长期运行 runtime 之上。**

重点是：
- 监控固定信息源
- 识别“变化”而不是重复摘要
- 对内容做分层判断
- 主动输出值得知道的信号

---

## 二、MVP 的真实目标

MVP 阶段不是追求“大而全”，而是先回答一个简单但难的问题：

> 能不能稳定把 AI 行业里的高价值变化，从一堆资讯里筛出来，并用比较像样的 brief 表达出来？

所以 MVP 不是做一个聊天壳，而是先做一个可运行的 intelligence pipeline。

---

## 三、核心模块

### 1. Source Registry
维护信息源配置：
- 名称
- 类型（rss / html / github_release / api）
- URL
- 抓取频率
- 默认主题标签
- 是否启用

### 2. Ingestion Pipeline
负责：
- 拉取原始内容
- 解析出 `title / summary / url / published_at / source`
- 归一化成统一事件结构

### 3. Dedup + Diff
负责：
- 同源去重
- 跨源粗去重
- 与上一次结果比较
- 标记新增、重复、持续升温项

### 4. Topic Classifier
先做规则版，覆盖最常见信号类型：
- model_release
- agent
- mcp
- open_source_model
- infra_compute
- eval_safety
- enterprise_adoption
- funding_policy

并逐步扩展到：
- tutorial_enablement
- case_study
- roundup_recap
- explainer_positioning
- capability_jump
- eval_infra
- tooling_ecosystem
- paper_style_explainer

### 5. Signal Ranker
先做启发式：
- 官方源优先
- 强信号关键词加分
- 教程 / 案例 / roundup 显式降权
- 结构变化型说明文豁免误杀
- 输出优先级分层

### 6. Report Generator
生成可读输出：
- 日报
- 午后复盘
- 变化摘要
- Top items
- 每条的“为什么值得看 / 洞察 / 后续关注”

### 7. Optional LLM Enrichment
作为增强层：
- 用于补自然语言洞察
- enrich 失败不影响主流程

### 8. Runtime Integration（后接）
在 MVP 后段或下一阶段接入：
- cron
- delivery
- memory
- 用户偏好

---

## 四、统一事件结构

```json
{
  "id": "stable_hash",
  "title": "Google unveils 8th gen TPU",
  "summary": "...",
  "url": "https://...",
  "source": "Google Blog",
  "published_at": "2026-04-30T07:00:00Z",
  "topics": ["infra_compute", "agent"],
  "signal_score": 0.87,
  "metadata": {
    "signal_bucket": "must_know",
    "reason": "带有平台分层/接口重构信号，可能改变成本结构和分发格局",
    "heuristic_insight": "...",
    "watch_next": "..."
  }
}
```

---

## 五、MVP 开发顺序

### Step 1
先做 source registry + ingestion

### Step 2
做统一事件结构 + 去重

### Step 3
做规则版 topic classifier + signal ranker

### Step 4
做日报 / 午报模板

### Step 5
做 snapshot diff / change detection

### Step 6
补“为什么值得看 / 洞察 / 后续关注”

### Step 7
再考虑接 runtime 的 cron / delivery / memory

---

## 六、为什么不先急着做 runtime 深集成

因为如果：
- 数据结构没想清楚
- 去重没做好
- 误判很多
- 报告模板不稳定

那即使接进 nanobot / OpenClaw，也只是把噪音更稳定地推送出去。

所以当前正确顺序是：

1. 先把 intelligence pipeline 本身定清楚
2. 再把它稳定挂到 runtime 上
3. 后续再决定是否做成更正式的 app / plugin / skill 形态

---

## 七、MVP 成功标准

如果 MVP 能做到下面这些，就算站住了：

- 能稳定抓固定源
- 能输出结构化事件
- 能做新增/重复/升温判断
- 能把明显教程/回顾/案例压到背景层
- 能把结构变化型、能力跃迁型内容保在高位
- 能给出比 topic 枚举更像样的“为什么值得看”解释
- 能通过定时任务稳定产出日报 / 午后复盘
