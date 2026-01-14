from fastapi import FastAPI

from vpn_sync.scheduler import start_scheduler, stop_scheduler
from vpn_sync.pinger import ping

app = FastAPI(title="VPN Sync Service")


@app.on_event("startup")
async def startup_event():
    start_scheduler()


@app.on_event("shutdown")
async def shutdown_event():
    stop_scheduler()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/run-once")
async def run_once():
    return await ping()
