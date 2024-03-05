# logs/logging_config.py
import atexit
import logging
import pathlib
import json
import logging
import logging.config
import logging.handlers

import os
import sys


# ! Log PYTHON PATH
# print("WITHIN LOGGING_CONFIG.PY\n\n")
# print(sys.path)
# print("-------------------\n")

# Passes in the name of the logger I want.
# logger = logging.getLogger("app")
logger = None


def setup_logging() -> int | None:
    global logger
    if logger is None:
        logger = logging.getLogger("app")
        logger.debug(msg="debug message", extra={"x": "hello"})

        config_file = pathlib.Path("logs/config.json")
        try:
            # Use the loaded config
            with open(config_file) as f_in:
                config = json.load(f_in)
        except FileNotFoundError:
            print(f"The file '{config_file}' was not found.")
        except PermissionError:
            print(f"Unable to read '{config_file}'.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in '{config_file}'.")

        logging.config.dictConfig(config)
        queue_handler = logging.getHandlerByName("queue_handler")
        if queue_handler is not None:
            queue_handler.listener.start()
            atexit.register(queue_handler.listener.stop)


def main():
    print("Logging Started.")
    logger.info("info message")
    pass


if __name__ == "__main__":
    setup_logging()
    main()
