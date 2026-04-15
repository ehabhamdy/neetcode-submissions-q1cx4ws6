class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l, r = 0, len(nums)-1
        res = nums[l]

        while l <= r:
            if nums[l] <= nums[r]:
                return min(res, nums[l])
                
            m = l + (r-l)//2
            print(m)
            res = min(res, nums[m])

            if nums[r] > nums[m]:
                r = m - 1    
            else:
                l = m + 1 

        return res