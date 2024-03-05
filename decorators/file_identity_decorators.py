# /LeetCode/decorators/file_identity_decorators.py
from functools import wraps


def location_of_file(func):
    # This is the wrapper function for the location_of_file decorator
    #
    @wraps(func)
    def wrapper(location_to_identify, *args, **kwargs):
        # Add logic related to the location of the file
        file_location_path = __file__
        print("Location of file: ")
        print(f"From Path: '{file_location_path}'.\n")
        return func(location_to_identify, *args, **kwargs)

    return wrapper  # return the wrapper function


def name_of_file(func):
    # This is the wrapper function for the name_of_file decorator
    @wraps(func)
    def wrapper(file_to_identify, *args, **kwargs):
        # Add logic related to the location of the file
        print("Name of file: ")
        print(f"Executing script: '{file_to_identify}'.\n")
        return func(file_to_identify, *args, **kwargs)

    return wrapper  # Return the wrapper function
