class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                ri, rh = stack.pop()
                area = (i - ri) * rh
                res = max(res, area)
                start = ri
            
            stack.append((start, h))

        for i, h in stack:
            area = (len(heights)-i) * h
            res = max(res, area)

        return res