from config import settings
from sync.client import get_url

_last_ping: dict | None = None


async def ping_once() -> dict:
    global _last_ping
    _last_ping = await get_url(settings.ping_url)
    return _last_ping


def get_last_ping() -> dict:
    return _last_ping or {"status": "no data yet"}
