class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        
        longest = 0
        for n in nums:
            length = 1
            if (n-1) in elements:
                length += 1
                while n+1 in elements:
                    length += 1
                    n  += 1
            longest = max(longest, length)
        
        return longest