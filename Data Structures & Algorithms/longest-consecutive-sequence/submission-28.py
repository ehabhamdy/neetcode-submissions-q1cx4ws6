class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        ns = set(nums)

        for i in range(len(nums)):
            l = 1
            while nums[i] + l in ns:
                l += 1

            res = max(res, l)

        return res