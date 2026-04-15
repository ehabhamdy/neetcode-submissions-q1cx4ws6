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
            while s[j] != '#':
                j += 1

            len_str = int(s[i:j])
            start_idx = j+1
            end_idx = start_idx + len_str
            res.append(s[start_idx: end_idx])

            i = end_idx

        return res
