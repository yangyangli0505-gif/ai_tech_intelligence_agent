"""Minimal ingestion pipeline."""

from __future__ import annotations

try:
    from .models import IngestionBatch
    from .source_registry import load_sources, enabled_sources
    from .rss_adapter import RSSAdapter
except ImportError:
    from models import IngestionBatch
    from source_registry import load_sources, enabled_sources
    from rss_adapter import RSSAdapter


ADAPTERS = [RSSAdapter()]


def run_ingestion() -> list[IngestionBatch]:
    batches: list[IngestionBatch] = []
    for source in enabled_sources(load_sources()):
        adapter = _pick_adapter(source)
        if adapter is None:
            batches.append(IngestionBatch(source=source.name, fetched_at="", events=[], errors=[f"No adapter for kind={source.kind}"]))
            continue
        batches.append(adapter.fetch(source))
    return batches


def _pick_adapter(source):
    for adapter in ADAPTERS:
        if adapter.supports(source):
            return adapter
    return None


if __name__ == "__main__":
    batches = run_ingestion()
    for batch in batches:
        print(f"\n=== {batch.source} ===")
        print(f"events={len(batch.events)} errors={len(batch.errors)}")
        for err in batch.errors:
            print(f"  ERROR: {err}")
        for event in batch.events[:3]:
            print(f"- {event.title} | {event.published_at}")
