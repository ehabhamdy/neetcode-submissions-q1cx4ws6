class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                ch, ci = stack.pop()
                area = ch * (i - ci)
                res = max(res, area)
                start = ci

            stack.append((h, start))

        for h, i in stack:
            area = h * (len(heights)-i)
            res = max(res, area)

        return res