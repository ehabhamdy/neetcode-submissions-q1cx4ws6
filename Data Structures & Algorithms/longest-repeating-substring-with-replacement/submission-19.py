from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        ml = 0

        l, r = 0, 0

        while r < len(s):
            chars[s[r]] += 1
            while chars and (r-l+1) - max(list(chars.values())) > k:
                chars[s[l]] -= 1
                l += 1

            ml = max(ml, (r-l+1))
            r += 1

        return ml
        