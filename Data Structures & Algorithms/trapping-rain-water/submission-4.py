class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r, res = 0, n-1, 0
        maxLeft, maxRight = height[l], height[r]

        if n == 0:
            return res
        
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]

            
        return res