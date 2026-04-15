class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        l = 1
        for i in range(len(nums)):
            res[i] = l
            l *= nums[i]
        
        print(res)

        d = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= d
            d *= nums[i]

        return res
        