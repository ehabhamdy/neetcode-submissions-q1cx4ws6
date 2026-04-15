class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxL = 0
        for i in range(len(nums)):
            if nums[i]-1 not in numSet:
                l = 1
                while l < len(nums) and nums[i]+l in numSet:
                    l += 1 
                maxL = max(maxL, l)


        return maxL 
