class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = []
        
        for i in range(len(s2)-(len(s1)-1)):
            s1key, s2key = [0]*26, [0]*26

            for c in s1:
                s1key[ord(c)-ord('a')] += 1 

            for c in s2[i:i+len(s1)]:
                s2key[ord(c)-ord('a')] += 1

            # match = 0
            # for i in range(26):
            #     if s1key[i] == s2key[i]:
            #         match += 1
                
            # if match == 26:
            #     return True
            if s1key == s2key:
                return True

        return False