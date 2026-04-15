from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = {'}': '{',']': '[',')': '(' }

        for c in s:
            if stack and closeToOpen.get(c) == stack[-1]:
                stack.pop()
            else:
                stack.append(c)


        if len(stack) == 0:
            return True
        
        return False

        
        