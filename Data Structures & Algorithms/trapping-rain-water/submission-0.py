class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        m = 0
        for h in height:
            leftMax.append(m)
            m = max(m, h)
        
        rightMax = [0] * len(height)
        m = 0
        for i in range(len(height)-1, -1, -1):
            rightMax[i] = m
            m = max(m, height[i])

        trapPerPosition = []
        for i in range(len(height)):
            trapPerPosition.append(max(0, min(leftMax[i], rightMax[i]) - height[i]))

        return sum(trapPerPosition)