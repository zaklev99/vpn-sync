import asyncio
import grpc

from rpc.generated import ping_pb2, ping_pb2_grpc


async def main():
    async with grpc.aio.insecure_channel("127.0.0.1:50051") as channel:
        stub = ping_pb2_grpc.PingServiceStub(channel)

        resp = await stub.PingOnce(ping_pb2.PingOnceRequest())
        print(resp)

if __name__ == "__main__":
    asyncio.run(main())
