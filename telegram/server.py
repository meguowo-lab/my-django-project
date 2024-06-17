from logging import Logger, getLogger
from concurrent import futures

import grpc.aio
from aiogram import Bot
from bot import Channel
from proto.api_pb2 import News, Response
from proto.api_pb2_grpc import ApiServicer, add_ApiServicer_to_server


class Api(ApiServicer):
    def __init__(self, ch: Channel, logger: Logger) -> None:
        self.ch = ch
        self.logger = logger
        super().__init__()

    async def send_news(self, request: News, context) -> Response:
        self.logger.info(f"news with title {request.title} sent...")

        await self.ch.send_news(
            request.author, request.title, request.url, request.image
        )
        self.logger.info(f"news with title {request.title} was succesfully sent!")

        return Response(message="ok")


async def run_server(ch: Channel, address: str):
    logger = getLogger("logger")

    logger.debug("Grpc server starts...")

    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ApiServicer_to_server(Api(ch, logger), server)
    server.add_insecure_port(address)
    await server.start()
    logger.debug("Grpc server succesfully started")

    await server.wait_for_termination()
