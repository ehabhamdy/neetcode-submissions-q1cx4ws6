class Solution:
    def isPalindrome(self, s: str) -> bool:
        ps = "".join([c.lower() for c in s if c.isalnum()])
        print(ps)
        return ps == ps[::-1]