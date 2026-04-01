class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char in close_to_open and len(stack) > 0 and close_to_open[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False