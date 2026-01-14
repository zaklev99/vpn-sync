import os
from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from vpn_sync.pinger import ping

PING_URL = os.getenv("PING_URL", "https://example.com")
PING_MINUTES = int(os.getenv("PING_MINUTES", "5"))

scheduler: AsyncIOScheduler | None = None


async def job() -> None:
    result = await ping(PING_URL)
    print("PING:", result, flush=True)


def start_scheduler() -> None:
    global scheduler
    if scheduler and scheduler.running:
        return

    scheduler = AsyncIOScheduler(executors={"default": AsyncIOExecutor()})
    scheduler.add_job(job, "interval", minutes=PING_MINUTES, max_instances=1, coalesce=True)
    scheduler.start()


def stop_scheduler() -> None:
    global scheduler
    if scheduler and scheduler.running:
        scheduler.shutdown(wait=False)
