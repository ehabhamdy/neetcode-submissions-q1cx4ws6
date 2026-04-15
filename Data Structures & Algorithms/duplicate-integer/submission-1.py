class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        hs = {nums[0]}
        for i in range(1, len(nums)):
            if nums[i] in hs:
                return True
            else:
                hs.add(nums[i])
        
        return False