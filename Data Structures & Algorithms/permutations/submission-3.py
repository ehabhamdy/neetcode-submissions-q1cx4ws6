class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)
        def dfs(nums, sol):
            if len(sol) == n:
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