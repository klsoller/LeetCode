"""
app.py
DOCUMENTATION
LICENSE: ALL RIGHTS RESERVED

Tutorial based on:
PyTest • REST API Integration Testing with Python
https://www.youtube.com/watch?v=7dgQRVqF1N0
"""

import os


os.system("cls")
import atexit
import logging
import logging.config
import logging.handlers

# from . import logger
# from . import setup_logging

import pathlib
import json


logger = logging.getLogger("app")  # Passes in the name of the logger I want.


# TODO: Configure this in the __init__ file.
def setup_logging():
    config_file = pathlib.Path("logs/config.json")
    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


def main():

    logger.debug(msg="debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except Exception:
        logger.exception("exception message\n")


if __name__ == "__main__":
    setup_logging()
    main()
