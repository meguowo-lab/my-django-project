from typing import Any

from grpc import insecure_channel

from .proto.api_pb2 import News
from .proto.api_pb2_grpc import ApiStub

channel = insecure_channel("127.0.0.1:80")

stub = ApiStub(channel)


def send_news(title: str, author: str, url: str, img: bytes):
    stub.send_news(News(title=title, author=author, url=url, image=img))
