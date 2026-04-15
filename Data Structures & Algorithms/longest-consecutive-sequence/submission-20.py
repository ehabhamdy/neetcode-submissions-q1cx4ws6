class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxL = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i]-1 not in numSet:
                currL = 1
                while currL < len(nums) and nums[i]+currL in numSet:
                    currL += 1 
                    maxL = max(maxL, currL)


        return maxL 
