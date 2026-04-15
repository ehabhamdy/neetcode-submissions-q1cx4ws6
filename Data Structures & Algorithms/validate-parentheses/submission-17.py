class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        stack = []

        for c in s:
            if stack and closeToOpen.get(c) == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0