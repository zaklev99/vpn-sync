from fastapi import FastAPI

from sync.router import router as sync_router
from sync.scheduler import start_scheduler, stop_scheduler

from config import settings


app = FastAPI(title=settings.app_name)

app.include_router(sync_router)


@app.on_event("startup")
async def on_startup():
    start_scheduler()


@app.on_event("shutdown")
async def on_shutdown():
    stop_scheduler()


@app.get("/health")
def health():
    return {"status": "ok"}
