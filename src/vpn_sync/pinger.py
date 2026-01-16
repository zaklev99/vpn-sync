import time
import httpx

DEFAULT_URL = "https://example.com"


async def ping(url: str = DEFAULT_URL) -> dict:
    started = time.time()
    try:
        async with httpx.AsyncClient(timeout=10, follow_redirects=True) as client:
            r = await client.get(url)
            return {
                "ok": True,
                "url": str(r.url),
                "status_code": r.status_code,
                "elapsed_ms": int((time.time() - started) * 1000),
                "error": None,
            }
    except httpx.HTTPError as e:
        return {
            "ok": False,
            "url": url,
            "status_code": None,
            "elapsed_ms": int((time.time() - started) * 1000),
            "error": f"{type(e).__name__}: {e}",
        }