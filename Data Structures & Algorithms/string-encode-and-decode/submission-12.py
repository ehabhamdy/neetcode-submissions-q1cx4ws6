class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i=0
        print(s)
        while i < len(s):
            idx = i
            while s[idx] != "#":
                idx += 1
            
            lenStr = int(s[i: idx])
            start = idx+1
            end = start + lenStr
            res.append(s[start: end])

            i = end
        
        return res