# 2-Week Build Plan

## Week 1: Intelligence Pipeline First

### Day 1
- 建立 source registry 数据结构
- 明确首批信息源（OpenAI / Google / HF / GitHub Releases）

### Day 2
- 写 ingestion 接口规范
- 给不同 source type 定 parser contract

### Day 3
- 做统一事件结构
- 做 stable hash 去重键

### Day 4
- 做规则版 topic classifier
- 先覆盖 6~8 个主题标签

### Day 5
- 做启发式 signal ranker
- 定义“必须知道 / 值得关注 / 待观察”分层规则

### Day 6
- 做日报模板
- 做午后复盘模板

### Day 7
- 做 diff / timeline 原型
- 验证“和上次相比新增了什么”

## Week 2: Runtime Integration

### Day 8
- 设计 nanobot integration 边界
- 明确哪些是 standalone pipeline，哪些交给 runtime

### Day 9
- 接 cron 调度
- 支持固定时间生成日报 / 午报

### Day 10
- 接主动推送
- 支持主题过滤

### Day 11
- 加 company/topic timeline memory

### Day 12
- 加专题追踪卡
- 例如 OpenAI / Google / MCP / open-source weekly view

### Day 13
- 加 source health / fetch error handling
- 防止某个源挂了导致整体输出质量崩掉

### Day 14
- 整理 README
- 准备 demo story
- 提炼简历 bullet

## 里程碑

### M1
能抓固定源并输出结构化事件

### M2
能自动生成日报 + 午报

### M3
能判断“新增变化”而不是重复摘要

### M4
能接入 nanobot 定时主动推送
