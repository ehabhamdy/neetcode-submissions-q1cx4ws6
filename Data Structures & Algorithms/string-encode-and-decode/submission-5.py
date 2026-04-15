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
            j = i
            while s[j] != "#":
                j += 1

            len_str = int(s[i: j])
            start = j + 1
            
            end = start + len_str

            res.append(s[start:end])

            i = end
        
        return res