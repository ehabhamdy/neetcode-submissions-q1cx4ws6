class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            idx = i
            while stack and h < stack[-1][1]:
                ii, hh = stack.pop()
                res = max(res, (i-ii) * hh)
                idx = ii

            stack.append((idx, h))

        for i, h in stack:
            area = (len(heights)-i) * h
            res = max(res, area)

        return res