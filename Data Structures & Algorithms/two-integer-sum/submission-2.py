class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {comp:idx}
        comp = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in comp:
                print('found')
                return [comp[c], i]
            
            comp[nums[i]] = i

        