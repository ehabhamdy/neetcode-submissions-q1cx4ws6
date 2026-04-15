class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rs = set()
        res = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in rs:
                rs.remove(s[l])
                l += 1
            
            
            rs.add(s[r])
            res = max(res, r-l+1)

        return res
        
