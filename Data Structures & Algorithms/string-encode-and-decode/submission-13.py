class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0    
        while i < len(s):
            idx = i
    
            while s[idx] != '#':
                idx += 1 
            
            l = int(s[i: idx])
            start = idx+1
            end = start + l
            part = s[start: end]

            
            res.append(part)
            i = end
            
        # return 1
        return res