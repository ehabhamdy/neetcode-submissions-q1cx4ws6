class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = "".join([c.lower() for c in s if c.isalnum()])

        i, j = 0, len(ns)-1

        while i <= j:
            if ns[i] != ns[j]:
                return False
            
            i += 1
            j -= 1 

        return True