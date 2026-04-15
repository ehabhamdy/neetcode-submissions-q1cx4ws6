from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()

        closeToOpen = {'}': '{', ']': '[', ')': '('}

        for c in s:
            if len(d) and closeToOpen.get(c) == d[-1]:
                d.pop()
            else:
                d.append(c)
            
        if len(d) == 0:
            return True
        
        return False
