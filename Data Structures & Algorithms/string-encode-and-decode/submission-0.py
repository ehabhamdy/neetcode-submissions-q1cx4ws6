class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
            
        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            print(s[i:j])
            s_len = int(s[i:j])
            
            s_start_idx = j+1
            s_end_idx = s_start_idx + s_len
            res.append(s[s_start_idx:s_end_idx])

            i = s_end_idx

        return res