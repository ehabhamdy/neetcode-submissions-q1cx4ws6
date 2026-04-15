from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        openings = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if len(d) and openings.get(c, '') == d[-1]:
                d.pop()
            else:
                d.append(c)
            
        if len(d) == 0:
            return True

        return False