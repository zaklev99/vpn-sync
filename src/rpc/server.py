import asyncio
from typing import Optional

import grpc

from sync.service import ping_once, get_last_ping
from rpc.generated import ping_pb2, ping_pb2_grpc


def _dict_to_ping_result(data: dict) -> ping_pb2.PingResult:
    """
    Преобразуем dict (из client/service) в protobuf-ответ.
    """
    # Если вернулся {"status": "no data yet"}
    if data.get("status") == "no data yet":
        return ping_pb2.PingResult(note="no data yet")

    return ping_pb2.PingResult(
        ok=bool(data.get("ok", False)),
        url=str(data.get("url", "")),
        status_code=int(data.get("status_code") or 0),
        elapsed_ms=int(data.get("elapsed_ms") or 0),
        error=str(data.get("error") or ""),
        note="",
    )


class PingServiceServicer(ping_pb2_grpc.PingServiceServicer):
    """
    Реализация методов, которые описаны в .proto
    """

    async def PingOnce(self, request, context):
        result = await ping_once()
        return _dict_to_ping_result(result)

    async def GetLastPing(self, request, context):
        result = get_last_ping()
        return _dict_to_ping_result(result)


async def serve(host: str = "0.0.0.0", port: int = 50051) -> None:
    server = grpc.aio.server()
    ping_pb2_grpc.add_PingServiceServicer_to_server(PingServiceServicer(), server)

    listen_addr = f"{host}:{port}"
    server.add_insecure_port(listen_addr)

    await server.start()
    print(f"[gRPC] Server started on {listen_addr}", flush=True)
    await server.wait_for_termination()
