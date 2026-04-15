from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            k = [0] * 26

            for c in s:
                k[ord(c)-ord('a')] += 1
            
            res[tuple(k)].append(s)

        return list(res.values())