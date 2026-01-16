from fastapi import APIRouter

from sync.service import ping_once, get_last_ping

router = APIRouter(prefix="/sync", tags=["sync"])


@router.post("/run-once")
async def run_once():
    return await ping_once()


@router.get("/last-ping")
def last_ping():
    return get_last_ping()


@router.get("tests")
def tests():
    return get_last_ping()