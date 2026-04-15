class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)

        i = 0

        s1k = [0] * 26
        for c in s1:
            s1k[ord(c)-ord('a')] += 1

        while i < len(s2):
            s2k = [0] * 26

            subStr =  s2[i: i+window]
            
            for c in subStr:
                s2k[ord(c)-ord('a')] += 1
            print(subStr)
            print(s2k)
            if s1k == s2k:
                return True

            i += 1

        return False