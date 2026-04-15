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
            strLen = ""
            print(i)
            while s[i] != '#':
                strLen += s[i]
                i += 1
            print(strLen)
            l = int(strLen)
            print(l)
            sStart = i + 1
            sEnd = sStart + l
            res.append(s[sStart: sEnd])
            i = sEnd

        return res