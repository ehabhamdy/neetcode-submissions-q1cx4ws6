class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)
        def dfs():
            if len(sol) == n:
                res.append(sol[:])
                return

            for i in range(len(nums)):
                if nums[i] not in sol:
                    sol.append(nums[i])
                    dfs()
                    sol.pop()

        dfs()
        return res