class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        l = len(nums)

        def dfs(numbers):
            if sum(cur) == target:
                res.append(cur[::])
                return

            if sum(cur) > target or not numbers:
                return
            
            cur.append(numbers[0])
            dfs(numbers)
            cur.pop()
            dfs(numbers[1:])        

        dfs(nums)

        return res