class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0

        for n in nums:
            currSum = max(n, n+currSum)
            maxSub = max(maxSub, currSum)

        return maxSub