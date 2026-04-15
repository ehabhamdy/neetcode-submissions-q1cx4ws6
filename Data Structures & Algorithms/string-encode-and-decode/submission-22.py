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
            idx = i
            while s[idx] != '#':
                idx += 1
            l = int(s[i: idx])
            sStart = idx + 1
            sEnd = sStart + l
            res.append(s[sStart: sEnd])
            i = sEnd

        return res