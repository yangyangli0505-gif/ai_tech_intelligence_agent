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

    # consumer-facing product updates should usually rank below infra / release / eval signals
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
