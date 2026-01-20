from fastapi import FastAPI
import asyncio

from sync.router import router as sync_router
from sync.scheduler import start_scheduler, stop_scheduler
from rpc.server import serve as grpc_serve

from config import settings


grpc_task: asyncio.Task | None = None

app = FastAPI(title=settings.app_name)

app.include_router(sync_router)


@app.on_event("startup")
async def on_startup():
    start_scheduler()

    global grpc_task
    grpc_task = asyncio.create_task(grpc_serve())


@app.on_event("shutdown")
async def on_shutdown():
    stop_scheduler()

    global grpc_task
    if grpc_task:
        grpc_task.cancel()


@app.get("/health")
def health():
    return {"status": "ok"}
