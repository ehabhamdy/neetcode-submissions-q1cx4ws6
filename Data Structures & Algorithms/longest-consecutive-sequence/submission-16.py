class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            l = 1
            if (n-1) not in numSet:
                while n+l in numSet:
                    l += 1

            res = max(res, l)

        return res