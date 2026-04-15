class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in elements:
                length = 1
                while n+length in elements:
                    length += 1
                longest = max(longest, length)
        
        return longest