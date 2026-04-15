class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        res = 0 

        for i in range(len(nums)):
            if nums[i]-1 in numSet:
                continue

            curr = 1
            l = 1
            while nums[i]+l in numSet:
                curr += 1
                l += 1

            res = max(res, l)

        return res