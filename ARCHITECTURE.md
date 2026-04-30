# Architecture Sketch

```text
[Source Registry]
   ├─ OpenAI Blog
   ├─ Google Blog / DeepMind
   ├─ Hugging Face Blog
   ├─ Anthropic News
   ├─ GitHub Releases
   └─ Selected Media
          |
          v
[Ingestion Pipeline]
   fetch -> parse -> normalize
          |
          v
[Unified Event Store]
   {title, summary, source, url, published_at, topics, score}
          |
     +----+----+
     |         |
     v         v
[Dedup/Diff] [Topic Classifier]
     |         |
     +----+----+
          |
          v
[Signal Ranker]
          |
          v
[Report Generator]
   ├─ 08:00 Daily Brief
   ├─ 15:00 Midday Recap
   └─ Topic Tracking Card
          |
          v
[nanobot Runtime Integration]
   ├─ cron scheduling
   ├─ delivery
   ├─ session/memory
   └─ user preferences
```

## 分层说明

### 底层：信息处理层
- source registry
- ingestion
- normalization
- dedup

### 中层：情报理解层
- topic classification
- signal ranking
- change detection
- timeline maintenance

### 上层：agent runtime 层
- cron
- delivery
- memory
- proactive pushes
- user interaction

## 当前策略

先把“信息处理层 + 情报理解层”定型，再接入 nanobot。
