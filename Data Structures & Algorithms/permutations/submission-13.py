class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        def dfs():
            if len(perm) == len(nums):
                    res.append(perm[::])

            for n in nums:                
                if n not in perm:
                    perm.append(n)
                    dfs()
                    perm.pop()

        dfs()

        return res
