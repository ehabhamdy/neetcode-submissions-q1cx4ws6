class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_idx = [0] * 26
        for i in range(len(s1)):
            s1_idx[ord(s1[i])-ord('a')] += 1

        
        for i in range(len(s2)-len(s1)+1):
            ss = s2[i: i + len(s1)]
            ss_idx = [0] * 26
            for i in range(len(ss)):
                ss_idx[ord(ss[i])-ord('a')] += 1

            if ss_idx == s1_idx:
                return True


        return False

            