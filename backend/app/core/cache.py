"""Simple query-response cache to avoid re-hitting the LLM for repeated
common questions (e.g. "aarti timings today") across many users."""
import hashlib
import json
from app.core.memory import _redis_client, REDIS_AVAILABLE
from app.config import get_settings

settings = get_settings()


def _cache_key(query: str) -> str:
    normalized = query.strip().lower()
    digest = hashlib.sha256(normalized.encode()).hexdigest()
    return f"ekdanta:cache:{digest}"


def get_cached_response(query: str) -> dict | None:
    if not REDIS_AVAILABLE:
        return None
    raw = _redis_client.get(_cache_key(query))
    return json.loads(raw) if raw else None


def set_cached_response(query: str, payload: dict):
    if not REDIS_AVAILABLE:
        return
    _redis_client.set(_cache_key(query), json.dumps(payload), ex=settings.CACHE_TTL_SECONDS)
