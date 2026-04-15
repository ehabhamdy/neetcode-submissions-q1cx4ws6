class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            l = i
            while s[l] != '#':
                l += 1

            strLen = int(s[i: l])
            sStart = l + 1
            sEnd = sStart + strLen

            res.append(s[sStart:sEnd])
            
            i = sEnd 
        
        return res