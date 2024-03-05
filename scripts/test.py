# /LeetCode/scripts/test.py


import os
import sys

# from config import setup as pp

# pp.add_root_to_path()
# pp.set_pythonpath()

# from logs import mylogger


# ! Log PYTHON PATH
# print("WITHIN TEST.PY\n\n")
# print(sys.path)
# print("-------------------\n")


# import logging
# from logs import setup_logging
# from logs import Logger as logger
from logs import logger
from decorators import file_input_objects


import logs


@file_input_objects.log_arguments
def main():
    x = 5
    try:
        1 / 0
    except Exception:
        # logger.critical("critical message")
        # logger.error("error message")
        # logger.warning("warning message")
        logger.debug("debug message")
        # logger.debug(msg="debug message", extra={"x": "hello"})
        logger.info("info message")


if __name__ == "__main__":
    main()
