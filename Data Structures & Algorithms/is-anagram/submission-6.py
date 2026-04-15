class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        k = [0]*26
        for i in range(len(s)):
            k[ord(s[i])-ord('a')] += 1
            k[ord(t[i])-ord('a')] -= 1

        for n in k:
            if n != 0:
                return False

        return True
