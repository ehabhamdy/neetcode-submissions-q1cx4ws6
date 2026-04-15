class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        def dfs(nums, sol):
            if len(sol) == len(nums) + len(sol) and not nums:
                res.append(sol[:])
                return

            for i in range(len(nums)):
                val = nums.pop(i)
                sol.append(val)
                dfs(nums, sol)
                sol.pop()
                nums.insert(i, val)

        dfs(nums, sol)
        return res