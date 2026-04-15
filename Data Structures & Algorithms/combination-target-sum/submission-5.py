class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subs = []

        def dfs(nums, rem):
            if rem < 0  or not nums:
                return
            if rem == 0:
                res.append(subs[::])
                return 

            subs.append(nums[0])
            dfs(nums, rem-nums[0])

            subs.pop()
            dfs(nums[1:], rem)

        dfs(nums, target)
        return res
            
