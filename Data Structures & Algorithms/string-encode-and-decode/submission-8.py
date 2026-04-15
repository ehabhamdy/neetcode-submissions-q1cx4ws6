class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            l = i
            while s[l] != '#':
                l += 1

            strLen = int(s[i:l])
            print(strLen)
            start = l + 1
            end = l + strLen + 1
            res.append(s[start:end])

            i = end

        return res