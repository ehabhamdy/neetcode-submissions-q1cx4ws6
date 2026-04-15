class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            l = i + 1
            r = len(nums)-1

            if i > 0 and n == nums[i-1]:
                continue

            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([nums[l], n, nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        
        return res
