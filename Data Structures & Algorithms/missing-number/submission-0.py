class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        full = [i for i in range(len(nums)+1)]
        print(full)
        for n in full:
            xor_sum ^= n

        print(xor_sum)

        for n in nums:
            xor_sum ^= n

        return xor_sum