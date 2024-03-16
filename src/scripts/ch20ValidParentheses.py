class Solution:
    def isValid(self, s: str) -> bool:
        stack_dict = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack_add = ("(", "{", "[")
        stack_pull = (")", "}", "]")

        stack = []

        # print(list(zips))
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char in stack_add:
                stack.append(char)
                continue
            if char in stack_pull:
                if stack == []:
                    return False
                if stack.pop() == stack_dict[char]:
                    continue
                else:
                    return False
        if stack != []:
            return False
        return True
