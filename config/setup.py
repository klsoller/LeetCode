# /LeetCode/config/setup.py
import os
import sys


def add_root_to_path() -> None:
    root_folder = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(root_folder)


def set_pythonpath() -> None:
    root_folder = os.path.abspath(os.path.dirname(__file__))
    python_path = os.path.join(root_folder, "..", "..")
    os.environ["PYTHONPATH"] = python_path


if __name__ == "__main__":
    set_pythonpath()
    add_root_to_path()
    from scripts import test  # Import your main script

    test.main()  # Execute your main script
