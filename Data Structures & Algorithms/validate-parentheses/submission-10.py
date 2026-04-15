from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = {'}': '{',']': '[',')': '(' }

        for i in range(len(s)):
            if stack and closeToOpen.get(s[i]) == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])


        if len(stack) == 0:
            return True
        
        return False

        
        