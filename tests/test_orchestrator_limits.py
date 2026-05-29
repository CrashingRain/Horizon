from datetime import datetime, timezone

from src.models import Config, ContentItem, SourceType
from src.orchestrator import HorizonOrchestrator
from src.storage.manager import StorageManager


def _config(max_items_before_ai=None, max_important_items=None) -> Config:
    return Config.model_validate(
        {
            "version": "1.0",
            "ai": {
                "provider": "openai",
                "model": "gpt-4o",
                "api_key_env": "OPENAI_API_KEY",
            },
            "sources": {"hackernews": {"enabled": True}},
            "filtering": {
                "ai_score_threshold": 7.0,
                "time_window_hours": 24,
                "max_items_before_ai": max_items_before_ai,
                "max_important_items": max_important_items,
            },
        }
    )


def _item(index: int, score: float | None = None) -> ContentItem:
    return ContentItem(
        id=f"rss:test:{index}",
        source_type=SourceType.RSS,
        title=f"Item {index}",
        url=f"https://example.com/{index}",
        published_at=datetime(2026, 4, 24, tzinfo=timezone.utc),
        ai_score=score,
    )


def test_limit_items_for_analysis_caps_before_ai(tmp_path) -> None:
    orchestrator = HorizonOrchestrator(
        _config(max_items_before_ai=2), StorageManager(str(tmp_path))
    )
    items = [_item(i) for i in range(4)]

    limited = orchestrator._limit_items_for_analysis(items)

    assert [item.id for item in limited] == ["rss:test:0", "rss:test:1"]


def test_limit_important_items_keeps_top_ranked_items(tmp_path) -> None:
    orchestrator = HorizonOrchestrator(
        _config(max_important_items=2), StorageManager(str(tmp_path))
    )
    items = [_item(0, 9), _item(1, 8), _item(2, 7)]

    limited = orchestrator._limit_important_items(items)

    assert [item.id for item in limited] == ["rss:test:0", "rss:test:1"]
