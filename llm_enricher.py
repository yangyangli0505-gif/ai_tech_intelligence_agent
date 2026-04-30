"""Optional lightweight LLM enrichment for event explanations.

Design goal:
- If no LLM config is present, stay fully local and deterministic.
- If LLM config is available, enrich top events with more natural insights.
- Never block the pipeline on LLM failure; always degrade gracefully.
"""

from __future__ import annotations

import json
import os
import urllib.request
from typing import Any

try:
    from .models import IntelligenceEvent
except ImportError:
    from models import IntelligenceEvent


DEFAULT_BASE_URL = os.getenv("AI_INTEL_LLM_BASE_URL", "https://api.openai.com/v1")
DEFAULT_MODEL = os.getenv("AI_INTEL_LLM_MODEL", "gpt-4o-mini")
DEFAULT_API_KEY = os.getenv("AI_INTEL_LLM_API_KEY", "")


def llm_available() -> bool:
    return bool(DEFAULT_API_KEY)


def enrich_events(events: list[IntelligenceEvent], max_events: int = 8) -> list[IntelligenceEvent]:
    """Try to enrich top events with more natural-language insight.

    Fallback behavior:
    - If no API key: keep heuristic metadata untouched.
    - If request fails: keep heuristic metadata untouched.
    """
    if not events:
        return events
    if not llm_available():
        return events

    target = events[:max_events]
    try:
        enriched = _call_llm(target)
    except Exception:
        return events

    by_id = {item.get("event_id"): item for item in enriched if item.get("event_id")}
    for event in target:
        eid = event.ensure_id()
        item = by_id.get(eid)
        if not item:
            continue
        if "insight_cn" in item and item["insight_cn"]:
            event.metadata["llm_insight"] = item["insight_cn"]
        if "watch_next_cn" in item and item["watch_next_cn"]:
            event.metadata["watch_next"] = item["watch_next_cn"]
        if "importance_adjust" in item:
            try:
                adj = float(item["importance_adjust"])
                event.signal_score = max(0.0, min(1.0, round(event.signal_score + adj, 3)))
            except Exception:
                pass
    events.sort(key=lambda e: (-e.signal_score, e.published_at, e.title.lower()))
    return events


def _call_llm(events: list[IntelligenceEvent]) -> list[dict[str, Any]]:
    prompt_events = [
        {
            "event_id": e.ensure_id(),
            "title": e.title,
            "summary": e.summary[:500],
            "source": e.source,
            "topics": e.topics,
            "signal_score": e.signal_score,
        }
        for e in events
    ]

    system = (
        "You are an AI tech intelligence analyst. "
        "For each event, write short natural-language insight in Chinese. "
        "Focus on why the event matters for the AI/LLM/Agent industry, "
        "not generic summary. Also suggest one short 'watch next' angle. "
        "Return strict JSON array only."
    )
    user = {
        "events": prompt_events,
        "schema": {
            "event_id": "string",
            "insight_cn": "<= 45 Chinese chars, insightful not repetitive",
            "watch_next_cn": "<= 28 Chinese chars",
            "importance_adjust": "number in [-0.08, 0.08]",
        },
    }

    body = {
        "model": DEFAULT_MODEL,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(user, ensure_ascii=False)},
        ],
        "temperature": 0.2,
    }

    req = urllib.request.Request(
        DEFAULT_BASE_URL.rstrip("/") + "/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEFAULT_API_KEY}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode("utf-8"))

    content = payload["choices"][0]["message"]["content"]
    parsed = json.loads(content)
    if isinstance(parsed, dict) and "events" in parsed:
        parsed = parsed["events"]
    if not isinstance(parsed, list):
        raise ValueError("LLM did not return a JSON array")
    return parsed
