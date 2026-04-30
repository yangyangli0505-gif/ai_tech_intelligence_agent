"""Heuristic signal ranking for intelligence events."""

from __future__ import annotations

try:
    from .models import IntelligenceEvent
except ImportError:
    from models import IntelligenceEvent


HIGH_PRIORITY_TOPICS = {
    "model_release",
    "agent",
    "mcp",
    "infra_compute",
    "eval_safety",
}

MEDIUM_PRIORITY_TOPICS = {
    "open_source_model",
    "enterprise_adoption",
    "funding_policy",
}

LOW_SIGNAL_PATTERNS = [
    "tips",
    "fun facts",
    "celebrating",
    "summer travel",
    "organizing your space",
    "headphones",
    "how to",
    "get started",
    "settings",
    "watch ",
    "dialogues",
]

CONSUMER_PRODUCT_PATTERNS = [
    "translate",
    "travel",
    "photos",
    "chrome",
    "workspace",
    "videos",
    "headphones",
    "organizing your space",
]

STRONG_SIGNAL_PATTERNS = [
    "agentic era",
    "orchestration",
    "compute bottleneck",
    "cybersecurity",
    "inference tiers",
    "open-source spec",
    "tpu",
    "gpu",
    "launching",
]


def score_event(event: IntelligenceEvent) -> IntelligenceEvent:
    score = 0.0
    title_summary = f" {event.title} {event.summary} ".lower()

    if "official" in event.topics:
        score += 0.24

    for topic in event.topics:
        if topic in HIGH_PRIORITY_TOPICS:
            score += 0.13
        elif topic in MEDIUM_PRIORITY_TOPICS:
            score += 0.08

    keyword_boosts = {
        " release ": 0.10,
        " launch ": 0.10,
        " version ": 0.07,
        " agent ": 0.09,
        " agentic ": 0.10,
        " mcp ": 0.15,
        " orchestration ": 0.11,
        " security ": 0.10,
        " cybersecurity ": 0.12,
        " compute ": 0.10,
        " tpu ": 0.13,
        " gpu ": 0.13,
        " funding ": 0.08,
        " ipo ": 0.08,
        " benchmark ": 0.08,
        " eval ": 0.09,
        " reranker ": 0.05,
    }
    for keyword, boost in keyword_boosts.items():
        if keyword in title_summary:
            score += boost

    for phrase in STRONG_SIGNAL_PATTERNS:
        if phrase in title_summary:
            score += 0.06

    for phrase in LOW_SIGNAL_PATTERNS:
        if phrase in title_summary:
            score -= 0.20

    consumer_hits = sum(1 for phrase in CONSUMER_PRODUCT_PATTERNS if phrase in title_summary)
    if consumer_hits >= 1:
        score -= 0.10
    if consumer_hits >= 2:
        score -= 0.08

    if "google translate" in title_summary:
        score -= 0.18
    if "ads advisor" in title_summary:
        score -= 0.14
    if "summer" in title_summary:
        score -= 0.12

    score = max(0.0, min(1.0, round(score, 3)))
    event.signal_score = score
    event.metadata["signal_bucket"] = signal_bucket(score)
    event.metadata["reason"] = explain_score(event)
    event.metadata["heuristic_insight"] = explain_insight(event)
    event.metadata["watch_next"] = suggest_watch_next(event)
    return event


def explain_score(event: IntelligenceEvent) -> str:
    reasons: list[str] = []
    title_summary = f" {event.title} {event.summary} ".lower()

    if "official" in event.topics:
        reasons.append("官方来源")
    if "model_release" in event.topics:
        reasons.append("涉及模型/版本发布")
    if "agent" in event.topics:
        reasons.append("涉及 Agent / orchestration")
    if "mcp" in event.topics:
        reasons.append("涉及 MCP 生态")
    if "infra_compute" in event.topics:
        reasons.append("涉及算力/基础设施")
    if "eval_safety" in event.topics:
        reasons.append("涉及 eval / safety")
    if any(k in title_summary for k in ["launch", "release", "version"]):
        reasons.append("存在明显发布/升级信号")
    if any(k in title_summary for k in ["tpu", "gpu", "compute"]):
        reasons.append("可能影响模型成本或能力上限")

    if not reasons:
        reasons.append("作为背景补充保留")
    return "；".join(dict.fromkeys(reasons))


def explain_insight(event: IntelligenceEvent) -> str:
    topics = set(event.topics)
    if {"infra_compute", "model_release"} & topics and "agent" in topics:
        return "这条更像产业底座升级，可能直接影响后续 Agent 能力边界和部署成本。"
    if "eval_safety" in topics and "infra_compute" in topics:
        return "它说明行业瓶颈正在从单纯训练算力，转向评测、推理和系统效率。"
    if "mcp" in topics:
        return "这类信号通常不是单点功能更新，而是生态协议层正在成熟。"
    if "model_release" in topics:
        return "这类更新值得看它是不是能力边界变化，而不只是常规版本迭代。"
    if "enterprise_adoption" in topics:
        return "更值得关注的是它是否意味着 AI 能力正在进入真实商业闭环。"
    return "这条更适合作为行业背景信号，帮助判断热点主线而不是单点噪音。"


def suggest_watch_next(event: IntelligenceEvent) -> str:
    topics = set(event.topics)
    if "infra_compute" in topics:
        return "继续看成本、吞吐和部署节奏"
    if "agent" in topics:
        return "继续看是否出现真实工作流落地"
    if "eval_safety" in topics:
        return "继续看评测基准和安全边界变化"
    if "model_release" in topics:
        return "继续看是否伴随 API / 定价 / benchmark"
    if "funding_policy" in topics:
        return "继续看是否影响资本开支和监管走向"
    return "继续看是否被更多源重复验证"


def score_events(events: list[IntelligenceEvent]) -> list[IntelligenceEvent]:
    ranked = [score_event(e) for e in events]
    ranked.sort(key=lambda e: (-e.signal_score, e.published_at, e.title.lower()))
    return ranked


def signal_bucket(score: float) -> str:
    if score >= 0.72:
        return "must_know"
    if score >= 0.48:
        return "worth_watch"
    if score >= 0.22:
        return "background"
    return "observe"
