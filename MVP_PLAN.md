# MVP Plan

## 一、产品边界

这个项目不是通用聊天助手，也不是单纯新闻摘要器。

它是一个 **持续情报跟踪系统**，重点在：

- 监控固定信息源
- 识别“变化”而不是重复摘要
- 对主题做连续跟踪
- 主动推送值得知道的信息

---

## 二、核心模块

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
- 解析出 title / summary / url / published_at / source
- 归一化成统一事件结构

### 3. Dedup + Diff
负责：
- 同源去重
- 跨源粗去重
- 与上一次日报 / 午报结果比较
- 标记新增、重复、持续升温项

### 4. Topic Classifier
先做规则版：
- model_release
- agent
- mcp
- open_source_model
- infra_compute
- eval_safety
- enterprise_adoption
- funding_policy

后续再做 LLM 分类增强。

### 5. Signal Ranker
先做启发式：
- 官方源 > 二手媒体
- 多源重复提及加分
- release / version / launch / funding / security / benchmark 等关键词加分
- 与用户关注主题匹配加分

### 6. Report Generator
生成三类产物：
- 日报
- 午后复盘
- 专题追踪卡

### 7. Memory / Timeline
维护：
- 每个主题最近 7 天事件
- 每家公司最近事件流
- 上次推送摘要

---

## 三、统一事件结构

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
  "is_new": true,
  "related_entities": ["Google", "TPU", "Agentic AI"]
}
```

---

## 四、MVP 开发顺序

### Step 1
先做 source registry + ingestion pipeline

### Step 2
做统一事件结构 + 去重

### Step 3
做规则版 topic classifier + signal ranker

### Step 4
做日报 / 午报模板

### Step 5
做 diff / timeline

### Step 6
再考虑接 nanobot 的 cron / delivery / memory

---

## 五、为什么先不急着接 nanobot

因为如果：
- 数据结构没想清楚
- 去重和 diff 没做好
- 报告模板不稳定

那即使接进 nanobot，也只是在稳定地推送噪音。

所以当前正确顺序是：
1. 先把 intelligence pipeline 定清楚
2. 再把它嵌进 nanobot runtime

---

## 六、后续可扩展点

- GitHub release watcher
- 公司级时间线视图
- 用户关注主题权重
- 事件聚类
- “为什么这条重要”解释器
- 异常提醒（突然高频更新 / 多源同时报道）
- 专题报告（如 MCP 生态周报）
