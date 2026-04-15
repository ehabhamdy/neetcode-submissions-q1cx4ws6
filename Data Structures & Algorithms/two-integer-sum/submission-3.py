class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {} # value: index

        for i, n in enumerate(nums):
            if comp and (target-n) in comp:
                return [comp[target-n], i]
            
            comp[n] = i

        

       