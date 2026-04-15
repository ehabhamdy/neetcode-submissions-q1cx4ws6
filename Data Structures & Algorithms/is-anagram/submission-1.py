class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_d = defaultdict(int)
        t_d = defaultdict(int)
        for i in range(len(s)):
            s_d[s[i]] += 1
            t_d[t[i]] += 1

        return s_d == t_d