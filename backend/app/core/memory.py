"""
Conversation memory per session_id, stored in Redis (so it survives
process restarts / scales across multiple backend workers). Falls back
to an in-process dict if Redis is unreachable, so local dev without
Redis still works.
"""
import json
import redis
from app.config import get_settings

settings = get_settings()

_fallback_store: dict[str, list[dict]] = {}

try:
    _redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)
    _redis_client.ping()
    REDIS_AVAILABLE = True
except Exception:
    REDIS_AVAILABLE = False
    _redis_client = None


def _key(session_id: str) -> str:
    return f"ekdanta:memory:{session_id}"


def get_history(session_id: str) -> list[dict]:
    if REDIS_AVAILABLE:
        raw = _redis_client.get(_key(session_id))
        return json.loads(raw) if raw else []
    return _fallback_store.get(session_id, [])


def append_turn(session_id: str, user_msg: str, assistant_msg: str):
    history = get_history(session_id)
    history.append({"user": user_msg, "assistant": assistant_msg})
    history = history[-settings.MEMORY_TURNS:]

    if REDIS_AVAILABLE:
        _redis_client.set(_key(session_id), json.dumps(history), ex=settings.CACHE_TTL_SECONDS)
    else:
        _fallback_store[session_id] = history


def clear_history(session_id: str):
    if REDIS_AVAILABLE:
        _redis_client.delete(_key(session_id))
    else:
        _fallback_store.pop(session_id, None)
