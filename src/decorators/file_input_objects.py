# /LeetCode/decorators/file_input_objects.py

import logging
from functools import wraps
from functools import update_wrapper

# from logs import Logger as logger
from logs import logger


def log_arguments(func):
    # TODO: Log 'function' != FunctionName. stdout is fine.
    # ? I'm not sure why stdout is fine, but the log file records the wrapper as the function name. Need to figure this out.
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_str = ", ".join([repr(arg) for arg in args])
        kwarg_str = ", ".join([f"{key}={value!r}" for key, value in kwargs.items()])
        logger.info(f"{func.__name__=} called:[{arg_str=}, {kwarg_str=}]")
        # logger.info("log file, function={func.__name__}")

        return func(*args, **kwargs)

    # wrapper.__name__ = func.__name__
    # update_wrapper(wrapper, func)
    # wrapper.__name__ = func.__name__
    # wrapper.__module__ = func.__module__
    # wrapper.__doc__ = func.__doc__
    return wrapper


@log_arguments
def example_function(a, b, c=3):
    print(f"a = {a}, b = {b}, c = {c}\n")


example_function(1, 2, c=4)
