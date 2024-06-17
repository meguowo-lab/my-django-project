import os
from asyncio import run, get_event_loop, gather

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from bot import Channel
from dotenv import load_dotenv
from logger import setup_logger
from run_bot import run_bot
from server import run_server
from env import setup_env, get


async def run_app():
    setup_env(".env", False)

    setup_logger()

    s = load_dotenv("./.env")
    if not s:
        raise Exception("cannot find .env file")

    bot = Bot(
        get("BOT_TOKEN"),
        default=DefaultBotProperties(parse_mode="HTML"),
    )

    ch = Channel(bot=bot, channel_id=get("CHANNEL_ID"))


    await gather(run_bot(bot), run_server(ch, address=get("GRPC_ADDRESS")))

if __name__ == "__main__":
    run(run_app())
