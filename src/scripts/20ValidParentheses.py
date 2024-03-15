class Solution:
    def isValid(self, s: str) -> bool:
        x = (,)
        y = (,)
        z = (,']')
        stack_dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }


        stack_add = ('(','{','[')
        stack_pull = (')','}',']')

        stack = []

        print(list(zips))
        if len(s)%2 != 0:
            return false

        for char in s:
            if char in stack_add:
                stack.appen(char)
            if char in stack_pull:
                if stack.pop() == stack_dict[char]:
                    continue
                else
                    return False

                #stack.append = x[1]
