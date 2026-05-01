# AI Tech Intelligence Agent

一个面向 **AI / LLM / Agent 领域** 的垂直情报跟踪项目。  
它不是单纯的“新闻摘要机器人”，而是一个尝试持续回答下面这些问题的 intelligence pipeline：

- 今天 AI 行业里 **真正重要** 的变化是什么？
- 哪些内容只是教程、布道、案例、回顾，**不应该被误判成主信号**？
- 一条信息为什么值得看？它影响的是 **能力边界、平台结构、评测基础设施、治理预期，还是工具链生态**？
- 和上一轮相比，**新增了什么、哪些在升温、哪些只是重复延续**？

这个项目当前采用的是：

- **启发式规则优先**：保证系统在没有外部大模型时也能工作
- **可选 LLM enrich**：在核心排序完成后，用大模型增强洞察表达
- **长期运行 runtime 友好**：适合挂在 nanobot / OpenClaw 这类 agent runtime 上做定时推送和持续追踪

---

# 一句话定位

> 这是一个基于长期运行 Agent runtime 的 AI 技术情报管线，用来持续监控 AI / LLM / Agent 生态中的高价值变化，并输出“日报 / 复盘 / 变化摘要 / 后续关注点”。

---

# 1. 为什么要做这个项目

AI 行业信息有一个很明显的问题：

一方面，信息极多。

- OpenAI / Google / Anthropic / Meta / xAI 官方博客
- Hugging Face 社区技术文章
- GitHub releases
- 开源模型、评测、工具链、推理平台更新
- 各种“what is... / top 10 uses / recap / roundup / highlights”内容

另一方面，**真正值得跟踪的高价值信号并不多**。

一个人如果只是刷资讯流，通常会遇到几个问题：

1. **信息过载**：看了很多，但记不住真正重要的变化
2. **信号和噪音混在一起**：教程、案例、营销说明文，经常伪装成“重大更新”
3. **缺乏变化视角**：不知道今天和昨天相比，到底新发生了什么
4. **缺乏结构化判断**：知道“有条新闻”，但不知道它影响的是哪一层

所以这个项目不是想解决“怎么抓更多新闻”，而是想解决：

> **如何把 AI 行业的信息流，变成一个更像“情报流”的东西。**

---

# 2. 项目最终想回答的核心问题

这个项目希望持续回答四类问题：

## 2.1 今天最值得知道的变化是什么？
不是“今天有哪些文章”，而是“今天有哪些变化值得你花注意力”。

## 2.2 这条为什么重要？
不是只打个标签，而是解释：

- 它是在推动 **能力边界前移**？
- 还是在改写 **平台分层 / 接口结构 / 供给格局**？
- 还是在补齐 **评测 / 验证 / 生产基础设施**？
- 还是在影响 **治理 / 安全 / 合规 / 采购预期**？
- 还是只是 **教程 / 启用文 / roundup / 案例**？

## 2.3 这条应该被放在什么优先级？
项目会尝试把内容分成：

- 必须知道
- 值得关注
- 背景补充
- 待观察

## 2.4 接下来还要看什么？
每条内容除了“为什么值得看”，还应该给出：

- 它后面要看什么验证
- 它会不会扩散到更大生态
- 它有没有进入真实产品/生产环境

---

# 3. 为什么它不是普通新闻摘要器

一个普通摘要器做的通常是：

- 抓 RSS
- 摘要正文
- 排序
- 输出一份日报

这个项目想做得更深一层：

## 普通摘要器关注的是：
- 说了什么

## 这个项目更关注的是：
- **它算不算主信号**
- **它属于哪一类信号**
- **它为什么重要**
- **它和上一轮相比是不是新增变化**

所以这个项目更接近：

> **面向 AI 行业的垂直 intelligence pipeline**

而不是：

> “把 RSS 包一层 LLM 总结”的 demo。

---

# 4. 为什么选择 nanobot / OpenClaw 这类 runtime 来承载它

这个项目有一个明确的分层思想：

## runtime 层负责：
- 长期运行
- 定时任务（cron）
- 聊天入口
- 主动推送
- session / memory
- 用户偏好记忆
- 工具接入

## intelligence pipeline 层负责：
- source registry
- ingestion
- normalization
- dedup
- topic classification
- signal ranking
- change detection
- report generation
- typed reasoning

也就是说：

> **不重造 agent runtime，本项目只负责“情报理解”这一层。**

这是一个非常重要的定位决定。

如果没有这个决定，项目很容易走偏成：
- 又做一套聊天壳
- 又做一套工具调度
- 又做一套 memory runtime

那就会和 nanobot / OpenClaw 本身重复。

现在的定位更清楚：

> runtime 提供“长期运行能力”，本项目提供“垂直领域 intelligence 能力”。

---

# 5. 从 0 到 1 的构思全过程

下面是这个项目真正的演化路径。

## 阶段 0：先确定不是“再做一个通用 Agent”

最早就明确了一件事：

这个项目不想做成：
- 通用问答 agent
- 通用个人助理
- 通用知识管理机器人

而是要做成：

> **一个围绕 AI / LLM / Agent 行业变化，持续运行的垂直情报产品。**

这一步很关键，因为它决定了后面的系统目标不是“回答所有问题”，而是：

- 更像长期行业观察器
- 更像技术情报助手
- 更强调连续追踪，而不是单轮对话

---

## 阶段 1：先搭骨架，不先追求智能感

第一步没有上来就做复杂 LLM reasoning，而是先搭一个最小但完整的 pipeline：

- source registry
- RSS ingestion
- normalized event model
- dedup
- topic classifier
- signal ranker
- report generator

这一阶段解决的是：

> **先让系统能稳定跑通一条完整链路。**

也就是先证明：

- 可以从多个源拉到内容
- 可以统一成结构化事件
- 可以初步分类和排序
- 可以输出一份可读的简报

这一步对应的是项目最底层的“骨架期”。

---

## 阶段 2：加入变化检测，不再只是重复摘要

如果只是每天重新总结一遍，那它永远只是“日报生成器”。

所以第二步很快就引入了：

- snapshot 保存
- latest snapshot 对比
- added / repeated / escalated
- 变化摘要

这一步很重要，因为它让系统开始回答：

- 今天新增了什么
- 哪些只是重复延续
- 哪些主题在升温

也就是说，系统开始从“信息转述”走向“变化跟踪”。

这是 intelligence 产品和普通 summary bot 的一个分水岭。

---

## 阶段 3：报告开始像“brief”而不是日志

有了分类、排序、diff 之后，下一步不是继续堆源，而是把输出改得更像真正能看的 brief。

因此加入了：

- 一句话总结
- 今日最重要 3 条
- 必须知道 / 值得关注 / 背景补充 / 待观察
- 变化摘要
- 为什么值得看

这一步的目标是：

> **让输出从机器日志，变成一个勉强像分析简报的东西。**

---

## 阶段 4：引入“启发式优先 + 可选 LLM enrich”

项目没有把 LLM 放在最前面做主判断，而是采取了：

- **heuristics first**
- **LLM optional**

原因很现实：

1. 不能让整个系统完全依赖外部模型
2. 排序/分层这种核心逻辑需要可控
3. 如果前面的分类错了，LLM 只会把错误说得更漂亮

所以 LLM enrich 的定位被明确成：

- 可选增强层
- 用来补洞察表达
- 失败时不影响主流程

这一步让系统兼顾了：

- 可运行性
- 可解释性
- 表达质量

---

## 阶段 5：真正的难点出现——误判收敛

做到这里后，系统虽然“能跑”，但质量还不够拿得出手。

核心问题不是：
- 会不会抓内容

而是：
- **会不会把不该高排的东西错判成高价值信号**

于是项目进入最关键的一阶段：

> **误判收敛（Plan B）**

这一阶段不再追求加功能，而是专门盯真实输出中的错误类型。

---

# 6. 误判收敛：这一阶段具体做了什么

这一轮迭代是真正让项目开始像样的地方。

## 6.1 先压教程 / enablement / 布道内容

典型问题：

- `What is Codex?`
- `Top 10 uses for Codex at work`
- 各种 `how to` / `get started` / `academy`

这类内容的问题是：

- 对理解产品很有帮助
- 但它们不是新的行业主信号

所以项目加了专门的：

- `tutorial_enablement`
- `TUTORIAL_PATTERNS`
- 对 `infra_compute` / `agent` / `model_release` 的去污染处理
- 显式降权

目标不是删掉它们，而是：

> **让它们留在背景层，而不是跑到头条层。**

---

## 6.2 再压 case study / adoption 内容

典型问题：

- customer story
- used OpenAI
- used our API
- automates
- real-world impact

这类内容也重要，但它的重要性不是“行业边界变化”，而是：

> **证明真实落地需求存在。**

于是项目把它们单列成：

- `case_study`

并让解释口径改成：

- 提供落地采用证据
- 验证业务可行性

这样它们就不会和 frontier signal 混在一起。

---

## 6.3 识别 roundup / recap / monthly digest

典型问题：

- latest AI news
- roundup
- recap
- what we announced
- this month / this week

这类内容的特点是：

- 很容易因为标题“大而全”被错误高排
- 但本质上是二次汇总，不是一级新增信号

所以项目显式引入：

- `roundup_recap`
- `ROUNDUP_PATTERNS`
- 排序惩罚

这个动作非常值，因为它能明显抑制“看起来很像大新闻，实际上只是打包回顾”的内容。

---

## 6.4 不要把所有 explainer 都压掉

做降噪后很快发现另一个问题：

有些内容写法像官方说明文、介绍文，但本质其实是结构变化型信号。

比如：

- `An open-source spec for orchestration: Symphony`
- `New ways to balance cost and reliability in the Gemini API`
- `OpenAI models, Codex, and Managed Agents come to AWS`
- `Building the compute infrastructure for the Intelligence Age`

如果简单看到：
- `introducing`
- `what is`
- `here’s how`

就全压掉，会误杀非常多真正重要的结构性变化。

于是项目加了：

- `explainer_positioning`
- `STRUCTURAL_SIGNAL_PATTERNS`
- 结构性解释文豁免逻辑

这一步的目标是：

> **压掉一般说明文，但保住真正的结构变化信号。**

---

## 6.5 把政策 / 安全叙事单列出来

还有一类内容最容易被误判成“不是技术，就不重要”：

- cybersecurity
- account security
- policy
- regulation
- trust / safety

但它们常常会真实影响：

- 企业采购预期
- 合规成本
- 治理叙事
- 安全门槛

所以项目没有简单把它们当噪音，而是开始把它们看成：

> **治理 / 采购口径变化信号**

这让系统对“非能力型内容”的判断更成熟了一些。

---

## 6.6 给 Hugging Face 技术内容做更细的内部分类

开源技术文章是这个项目里最难处理的一类内容。

一开始 Hugging Face 内容太容易全落入：

- `eval_safety`
- `open_source_model`

但实际上它们内部差异极大。

所以后面专门拆出 4 类：

### `capability_jump`
代表能力边界前移，比如：
- 更强长上下文
- 更强可交互世界建模
- 更强可用 agent context

### `eval_infra`
代表评测/验证基础设施增强，比如：
- 评测瓶颈
- benchmark infra
- 可复现评估链路

### `tooling_ecosystem`
代表工具链生态扩展，比如：
- inference providers
- 模型分发/接入层变化
- 开发者工作流增强

### `paper_style_explainer`
代表论文式说明/方法分析，通常认知价值高，但未必是主信号

这一层细分让 Hugging Face 内容不再“一锅端”，是当前质量提升里很关键的一步。

---

## 6.7 修 source-aware 污染问题

后面又发现一个更隐蔽的问题：

Hugging Face 专用的技术子类规则，会错误污染其他来源内容。

比如：
- Google Gemini API 某些文章，被误挂成 `paper_style_explainer`

这个问题后面通过 source-aware 规则收掉了：

- HF 专属细分标签只对 `huggingface_blog` 生效
- 非 HF 源不再复用这套子类判断

这个修正很重要，因为它解决的是：

> **一个来源的语言风格规则，污染另一个来源。**

---

# 7. “为什么值得看”是怎么一步步演化的

这是本项目最近一轮最明显的变化。

## 最早版本
最早的解释更像 topic 枚举：

- 官方来源
- 涉及模型发布
- 涉及 Agent
- 涉及基础设施
- 涉及 eval/safety

问题是：

- 看起来像解释
- 其实还是标签堆叠
- 不够像分析判断

---

## 中间版本
后面开始加一点语义：

- 偏教程/启用内容
- 偏案例/采用信号
- 偏回顾/汇总内容
- 可能影响模型成本、性能、分发或可用性

这一步比纯 topic 好，但仍然偏泛。

---

## 当前版本
现在“为什么值得看”已经开始变成 **typed reasoning**，会按不同类型给出不同口径。

例如：

### 能力跃迁型
- 带有能力边界前移信号
- 可能改写现有产品形态或训练方式

### 评测基础设施型
- 带有评测/验证基础设施成熟信号
- 关系到 Agent 从 demo 到生产

### 平台结构变化型
- 带有平台分层/接口重构信号
- 可能改变成本结构和分发格局

### 治理/采购叙事型
- 带有治理/采购口径变化信号
- 会影响合规、风险和企业预期

### 工具链生态型
- 带有工具链成熟度提升信号
- 会影响开发效率和生态采用速度

这一步的意义非常大，因为它代表系统开始从：

- “知道它属于什么类”

走向：

- “知道它为什么重要”

---

# 8. 当前系统架构

当前核心流程如下：

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
   └─ 变化摘要 / Top items / 分层简报
          |
          v
 [Optional LLM Enrichment]
          |
          v
 [Runtime Delivery]
   via nanobot / OpenClaw cron + messaging
```

---

# 9. 当前已经具备的能力

截至当前版本，项目已经具备：

## 数据处理层
- 多源 RSS 抓取
- 统一事件结构
- 去重
- source registry

## 情报理解层
- topic classification
- signal ranking
- typed reasoning
- heuristic insight
- watch next
- snapshot diff / change detection

## 报告输出层
- 日报预览
- 午后复盘预览
- 必须知道 / 值得关注 / 背景补充 / 待观察
- 一句话总结
- Top 3 重点条目
- 每条的“为什么值得看 / 洞察 / 后续关注”

## 增强层
- optional LLM enrichment
- OpenAI-compatible endpoint 支持
- 已验证 `https://aixor.org/v1`
- 默认 enrich 模型口径为 `gpt-5.4`

---

# 10. 项目怎么用

## 10.1 本地运行
在项目目录下运行：

```bash
python3 ingest.py
```

它会完成：

1. 抓取已配置源
2. 标准化为统一事件
3. 去重
4. 分类
5. 排序
6. 做 snapshot diff
7. 生成一版 brief preview

---

## 10.2 启用 LLM enrich（可选）
可以通过环境变量启用：

```bash
AI_INTEL_LLM_API_KEY=your_key
AI_INTEL_LLM_BASE_URL=https://aixor.org/v1
AI_INTEL_LLM_MODEL=gpt-5.4
python3 ingest.py
```

说明：

- LLM enrich 是可选增强层
- 没有 key 时，系统仍能使用启发式逻辑正常工作
- enrich 失败不会阻塞主流程

---

## 10.3 接到长期运行 runtime 上
适合接在 nanobot / OpenClaw 上做：

- 08:00 日报推送
- 15:00 午后复盘
- 未来可以扩展为：
  - company/topic tracking
  - 异常提醒
  - 周报
  - 特定主题观察卡

---

# 11. 这个项目能应用在哪些场景

## 场景 1：个人 AI 行业信息跟踪
如果你每天都想知道：

- OpenAI / Google / Anthropic 最近在干什么
- 哪些更新真的值得看
- 哪些只是说明文、案例、营销回顾

这个项目可以每天自动给你一版更有判断力的技术简报。

---

## 场景 2：产品经理 / 创业者 / 研究者做行业扫描
他们通常不是缺信息，而是缺：

- 更稳定的持续追踪
- 更少噪音
- 更像“结构化观察”的输出

这个项目可以帮助他们快速判断：

- 行业主线在往哪走
- 哪些变化属于底层结构变化
- 哪些只是局部功能升级

---

## 场景 3：Agent / LLM 应用团队做竞争情报
对于在做：

- Agent
- inference platform
- AI infra
- developer tooling
- evaluation platform

的团队来说，持续跟踪以下变化很重要：

- 谁在改 API 分层
- 谁在做新协议/接口
- 谁在补评测基础设施
- 谁在通过生态接入改变分发格局

这个项目非常适合做成内部情报助手。

---

## 场景 4：长期主题观察
它未来也适合做：

- OpenAI 近 7 天变化
- MCP 生态周追踪
- 开源模型能力跃迁追踪
- Agent 长任务/评测基础设施专题追踪

这会比“单次搜索”更接近真实使用价值。

---

# 12. 这个项目的意义是什么

我觉得这个项目真正的意义，不在于“又做了一个资讯机器人”。

而在于它试图回答一个更现实的问题：

> **当 AI 行业信息爆炸时，怎么把连续的信息流，整理成有层次、有优先级、有解释的技术情报流。**

它的意义主要有三层：

## 12.1 从信息消费，走向信号理解
不是“看更多”，而是“看对东西”。

## 12.2 从摘要，走向结构化判断
不是“这篇讲了什么”，而是“这条影响的是哪一层”。

## 12.3 从单轮总结，走向持续跟踪
不是“生成一篇日报”，而是“把行业变化作为一个连续系统来观察”。

---

# 13. 当前成熟度判断

实话说，项目现在：

## 还不是成品
它还没有完全达到：

- 足够稳定
- 足够泛化
- 每天都放心自动发
- 很少误判

的程度。

---

## 但已经不是玩具
因为它已经具备：

- source-aware 规则
- 类型边界处理
- 误判收敛逻辑
- 类型化解释层
- LLM enrich + fallback
- 变化检测视角

所以它已经不再只是一个“能总结资讯”的脚本，而是开始像：

> **一个认真尝试做 AI 行业信号识别与解释的垂直项目。**

---

# 14. 后续还能怎么继续迭代

下一阶段我认为更值得做的是：

## 14.1 继续用真实输出做校准
观察几天到一周真实结果，看还有哪些误判在冒头。

## 14.2 报告展示层继续抛光
让输出更像成品，而不是工程预览。

## 14.3 扩展更高价值的信息源
在不明显加噪音的前提下，增加：

- GitHub releases
- selected docs updates
- 更少量但更高信噪比的官方源

## 14.4 增加专题视图
例如：

- company view
- topic timeline
- weekly delta
- capability jump tracker

---

# 15. 当前相关文件

核心文件包括：

- `models.py`：统一事件模型
- `source_registry.py`：信息源注册
- `rss_adapter.py`：RSS 拉取与适配
- `dedup.py`：去重
- `topic_classifier.py`：主题分类与类型边界处理
- `signal_ranker.py`：信号排序、typed reasoning、洞察、watch-next
- `change_detection.py`：快照 diff / 变化检测
- `report_generator.py`：报告生成
- `llm_enricher.py`：可选 LLM enrich
- `ingest.py`：主流程入口

文档文件包括：

- `ARCHITECTURE.md`
- `BUILD_PLAN.md`
- `MVP_PLAN.md`
- `RESUME_POSITIONING.md`

---

# 16. 当前阶段一句话总结

> 这个项目已经从“会抓、会排、会写”的资讯流水线，推进到了“开始会判断内容类型、解释价值机制”的 intelligence pipeline 阶段。
