class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ist, hst = stack.pop()
                area = hst * (i - ist)
                res = max(res, area)
                start = ist

            stack.append((start, h))

        for i, h in stack:
            area = h * (len(heights)-i)
            res = max(res, area)

        return res