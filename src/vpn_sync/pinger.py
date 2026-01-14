import httpx

DEFAULT_URL = "https://example.com"


async def ping(url: str = DEFAULT_URL) -> dict:
    async with httpx.AsyncClient(timeout=10, follow_redirects=True) as client:
        r = await client.get(url)
        return {"url": str(r.url), "status_code": r.status_code}
