class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break


            m = l + (r-l)//2
            res = min(res, nums[m])

            if nums[m] >= nums[l]: # that means that the minimum will be in the right part of the array
                l = m + 1
            else:
                r = m - 1

        
        return res