from config import settings
from notify.factory import build_notifier
from sync.client import get_url

_last_ping: dict | None = None
_notifier = build_notifier()


async def ping_once() -> dict:
    global _last_ping

    result = await get_url(settings.ping_url)
    _last_ping = result

    # если пинг не удался — шлём уведомление
    if not result.get("ok") and _notifier:
        text = (
            "🚨 VPN-SYNC ALERT\n"
            f"URL: {result.get('url')}\n"
            f"Error: {result.get('error')}\n"
            f"Time: {result.get('elapsed_ms')} ms"
        )
        await _notifier.send(text)

    return _last_ping


def get_last_ping() -> dict:
    return _last_ping or {"status": "no data yet"}
