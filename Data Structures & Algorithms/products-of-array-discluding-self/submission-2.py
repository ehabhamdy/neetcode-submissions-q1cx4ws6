class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        pref = 1 
        p_array = []
        for i in range(len(nums)):
            p_array.append(pref)
            pref *= nums[i]

        post = 1
        post_array = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            post_array[i] = post
            post *= nums[i]
        
        print(p_array)
        print(post_array)
        res = []
        for i in range(len(nums)):
            res.append(p_array[i] * post_array[i])

        return res

        # [1, 1, 2, 8]
        # [48,24,6,1]

        # [48, 24, 12, 8]