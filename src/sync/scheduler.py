from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import settings
from sync.service import ping_once

scheduler: AsyncIOScheduler | None = None


def start_scheduler() -> None:
    global scheduler
    if scheduler and scheduler.running:
        return

    scheduler = AsyncIOScheduler(executors={"default": AsyncIOExecutor()})
    scheduler.add_job(
        ping_once,
        "interval",
        minutes=settings.ping_minutes,
        max_instances=1,
        coalesce=True,
    )
    scheduler.start()


def stop_scheduler() -> None:
    global scheduler
    if scheduler and scheduler.running:
        scheduler.shutdown(wait=False)
