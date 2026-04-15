class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r, res = 0, n-1, 0
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                res += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                res += max(0, maxR - height[r])
                maxR = max(maxR, height[r])

        return res