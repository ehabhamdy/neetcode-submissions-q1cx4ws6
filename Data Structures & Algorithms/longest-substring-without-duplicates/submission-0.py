class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        r = 0
        
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            res = max(res, r-l+1)
            charSet.add(s[r])
            r += 1

        return res