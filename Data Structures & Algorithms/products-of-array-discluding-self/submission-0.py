class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        result = []

        for i in range(len(nums)):
            prefix = 1
            if i > 0:
                for j in range(0, i):
                    prefix *= nums[j]
            result.append(prefix)

        print(result)
        for i in range(len(nums)-1, -1, -1):
            postfix = 1
            if i < len(nums)-1:
                for j in range(i+1, len(nums)):
                    postfix *= nums[j]
            
            result[i] = postfix * result[i]

        return result

# nums=[1,2,4,6]
# [1,1,2,8]