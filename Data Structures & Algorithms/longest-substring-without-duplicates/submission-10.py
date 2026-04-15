class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        unique = set()

        l = r = 0

        while r < len(s):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            
            unique.add(s[r])
            longest = max(longest, len(unique))
            r += 1

        return longest
