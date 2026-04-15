class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def dfs(i, rem):
            if rem == 0:
                res.append(sub.copy())
                return
            
            if i >= len(nums) or rem < 0:
                return

            sub.append(nums[i])
            dfs(i, rem - nums[i])

            sub.pop()
            dfs(i+1, rem)

        dfs(0, target)

        return res