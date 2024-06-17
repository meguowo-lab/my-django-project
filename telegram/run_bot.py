from aiogram import Bot, Dispatcher
from logging import getLogger, Logger


def startup(logger: Logger):
    def wrapper():
        logger.debug("Telegram bot succesfully started!")

    return wrapper

def shutdown(logger: Logger):
    def wrapper():
        logger.debug("Telegram bot shutdowns...")

    return wrapper


async def run_bot(bot: Bot):
    logger = getLogger("logger")

    logger.debug("Telegram bot starts...")
    dp = Dispatcher()

    dp.startup.register(startup(logger))
    dp.shutdown.register(shutdown(logger))

    await dp.start_polling(bot)
