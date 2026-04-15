class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        
        def dfs():
            if len(sub) == len(nums):
                    res.append(sub.copy())
                    return
            for i, n in enumerate(nums):
                if n not in sub:
                    sub.append(n)
                    dfs()
                    sub.pop()

        dfs()
        return res