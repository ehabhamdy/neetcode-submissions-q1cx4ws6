class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {
            '[': ']',
            '(': ')',
            '{': '}'
        }

        for c in s:
            if len(stack) and openToClose.get(stack[-1]) == c:
                stack.pop()
                continue

            stack.append(c)

        if len(stack):
            return False

        return True