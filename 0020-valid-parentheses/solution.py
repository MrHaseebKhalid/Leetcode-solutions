class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        n = len(s)
        stack = []

        if n != 0 and n % 2 == 0:
            for x in s:
                if x in valid:
                    stack.append(x)
                else:
                    if stack == [] or valid[stack.pop()] != x:
                        return False
            return stack == []
        return False
