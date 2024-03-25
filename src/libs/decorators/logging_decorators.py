# /LeetCode/decorators/logging_decorators.py

from functools import wraps


def log_decorator_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass

    return wrapper
