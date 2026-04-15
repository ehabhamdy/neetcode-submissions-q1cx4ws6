class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = [0]*26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            anagram[ord(s[i])-ord('a')] += 1
            anagram[ord(t[i])-ord('a')] -= 1

        for n in anagram:
            if n != 0:
                return False

        return True