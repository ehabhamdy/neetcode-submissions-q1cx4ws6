class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i, total):
            if total < 0 or i >= len(nums):
                return

            if total == 0:
                res.append(sub.copy())
                return

            sub.append(nums[i])
            dfs(i, total-nums[i])
            sub.pop()
            dfs(i+1, total)

        dfs(0, target)
        return res


