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

            sl = int(s[i:idx])

            ss = idx+1
            se = ss+sl

            res.append(s[ss:se])

            i = se
        
        return res

