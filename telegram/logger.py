import sys
from logging import DEBUG, INFO, Formatter, Handler, StreamHandler, getLogger, FileHandler, Logger

def add_handler(logger: Logger, handler: Handler, level: int | str):
    handler.setLevel(level)
    handler.setFormatter(Formatter("[%(levelname)s] %(asctime)s - %(message)s"))
    logger.addHandler(handler)

def setup_logger():
    logger = getLogger("logger")
    logger.setLevel(DEBUG)

    add_handler(logger, StreamHandler(sys.stdout), DEBUG)

    add_handler(logger, FileHandler("logs/info.log"), INFO)

    add_handler(logger, FileHandler("logs/debug.log"), DEBUG)

    logger.debug("succesfully setuped logger")
