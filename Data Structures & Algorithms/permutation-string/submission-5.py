class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-(len(s1)-1)):
            s1k, s2k = [0]*26, [0]*26

            for c in s1:
                s1k[ord(c)-ord('a')] += 1

            for c in s2[i: i+len(s1)]:
                s2k[ord(c)-ord('a')] += 1

            if s1k == s2k:
                return True
        
        return False