"""Rule-based topic classification for intelligence events."""

from __future__ import annotations

try:
    from .models import IntelligenceEvent
except ImportError:
    from models import IntelligenceEvent


TOPIC_RULES: dict[str, list[str]] = {
    "model_release": [
        "model", "release", "launch", "version", "gemini", "gpt", "claude", "llama", "granite",
    ],
    "agent": [
        "agent", "agents", "agentic", "workflow", "browser use", "tool use", "automation",
    ],
    "mcp": [
        "mcp", "model context protocol",
    ],
    "infra_compute": [
        "gpu", "tpu", "compute", "datacenter", "data center", "inference", "training", "chip", "chips",
    ],
    "eval_safety": [
        "eval", "evaluation", "safety", "alignment", "cybersecurity", "security", "benchmark",
    ],
    "open_source_model": [
        "open source", "hugging face", "weights", "checkpoint", "granite", "mistral",
    ],
    "enterprise_adoption": [
        "enterprise", "business", "workspace", "customer", "cloud", "deployment", "productivity",
    ],
    "funding_policy": [
        "funding", "investment", "capital", "policy", "regulation", "government", "acquisition", "ipo",
    ],
}


def classify_event(event: IntelligenceEvent) -> IntelligenceEvent:
    haystack = f"{event.title} {event.summary}".lower()
    topics = set(event.topics)

    for topic, keywords in TOPIC_RULES.items():
        if any(k in haystack for k in keywords):
            topics.add(topic)

    if not topics:
        topics.add("general_ai")

    event.topics = sorted(topics)
    return event


def classify_events(events: list[IntelligenceEvent]) -> list[IntelligenceEvent]:
    return [classify_event(event) for event in events]
