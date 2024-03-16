# /LeetCode/tests/test_LeetCode.py

import os
import sys
import pytest

# from src.logs import logger
# from src.decorators import file_input_objects
from src.scripts import ch20ValidParentheses as ch20


class Test_ch20:
    # pass

    def test_case1(self) -> None:
        test_input = "()"
        # print(f"{test_input=}")
        assert ch20.Solution().isValid(test_input) == True

    def test_case2(self) -> None:
        test_input = "()[]{}"
        print(f"{test_input=}\n\n\n")
        assert ch20.Solution().isValid(test_input) == True

    def test_case3(self) -> None:
        test_input = "(]"
        # print(f"{test_input=}")
        assert ch20.Solution().isValid(test_input) == False

    def test_case4(self) -> None:
        test_input = "([{}])"
        # print(f"{test_input=}")
        assert ch20.Solution().isValid(test_input) == True


if __name__ == "__main__":
    pytest.main()
