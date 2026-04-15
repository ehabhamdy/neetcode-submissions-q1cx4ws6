class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        def dfs():
            for n in nums:
                if len(perm) == len(nums) and perm not in res:
                    res.append(perm[::])

                if n not in perm:
                    perm.append(n)
                    dfs()
                    perm.pop()

        dfs()

        return res
