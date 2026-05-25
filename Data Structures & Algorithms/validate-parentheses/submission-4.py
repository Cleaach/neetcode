class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if not stack or p in "[{(":
                stack.append(p)
            else:
                if p == "]":
                    if stack.pop() != "[":
                        return False
                if p == ")":
                    if stack.pop() != "(":
                        return False
                if p == "}":
                    if stack.pop() != "{":
                        return False
        if not stack:
            return True
        else:
            return False