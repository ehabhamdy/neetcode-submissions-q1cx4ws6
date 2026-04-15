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
            print(s[i:l])
            strLen = int(s[i:l])

            strS = l + 1
            strE = strS + strLen

            res.append(s[strS: strE])

            i = strE 

        return res