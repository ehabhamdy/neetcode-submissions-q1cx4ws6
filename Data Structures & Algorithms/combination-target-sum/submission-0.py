from collections import Counter
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        partial = []

        def dfs():
            if sum(partial) > target:
                return

            

            if sum(partial) == target:
                for l in res:
                    if Counter(l) == Counter(partial):
                        return
                res.append(partial[::])
                return 

            for i in range(len(nums)):
                partial.append(nums[i])
                dfs()
                partial.pop()

        dfs()

        return res