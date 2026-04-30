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
]


def score_event(event: IntelligenceEvent) -> IntelligenceEvent:
    score = 0.0
    title_summary = f" {event.title} {event.summary} ".lower()

    if "official" in event.topics:
        score += 0.26

    for topic in event.topics:
        if topic in HIGH_PRIORITY_TOPICS:
            score += 0.14
        elif topic in MEDIUM_PRIORITY_TOPICS:
            score += 0.08

    keyword_boosts = {
        " release ": 0.10,
        " launch ": 0.10,
        " version ": 0.07,
        " agent ": 0.09,
        " agentic ": 0.10,
        " mcp ": 0.15,
        " orchestration ": 0.10,
        " security ": 0.10,
        " cybersecurity ": 0.12,
        " compute ": 0.10,
        " tpu ": 0.12,
        " gpu ": 0.12,
        " funding ": 0.08,
        " ipo ": 0.08,
        " benchmark ": 0.08,
        " eval ": 0.08,
    }
    for keyword, boost in keyword_boosts.items():
        if keyword in title_summary:
            score += boost

    for phrase in LOW_SIGNAL_PATTERNS:
        if phrase in title_summary:
            score -= 0.24

    if "google translate" in title_summary:
        score -= 0.18
    if "ads advisor" in title_summary:
        score -= 0.10

    score = max(0.0, min(1.0, round(score, 3)))
    event.signal_score = score
    return event


def score_events(events: list[IntelligenceEvent]) -> list[IntelligenceEvent]:
    ranked = [score_event(e) for e in events]
    ranked.sort(key=lambda e: (-e.signal_score, e.published_at, e.title.lower()))
    return ranked


def signal_bucket(score: float) -> str:
    if score >= 0.70:
        return "must_know"
    if score >= 0.45:
        return "worth_watch"
    if score >= 0.20:
        return "background"
    return "observe"
