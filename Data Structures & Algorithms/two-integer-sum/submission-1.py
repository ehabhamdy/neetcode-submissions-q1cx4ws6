class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {v: i for (i, v) in enumerate(nums)}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in nums[i+1:]:
                return [i, d[c]] 