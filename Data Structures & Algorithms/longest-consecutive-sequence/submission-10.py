class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        res = 0

        for i, n in enumerate(nums):
            l = 0
            if n-1 not in s:
                while n+l in s:
                    l +=1 

                res = max(res, l) 

        return res