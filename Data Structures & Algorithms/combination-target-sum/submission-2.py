class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(numbers, remaining):
            if remaining == 0:
                res.append(cur[::])
                return

            if remaining < 0 or not numbers:
                return
            
            cur.append(numbers[0])

            dfs(numbers, remaining - numbers[0])

            cur.pop()
            
            dfs(numbers[1:], remaining)        

        dfs(nums, target)

        return res