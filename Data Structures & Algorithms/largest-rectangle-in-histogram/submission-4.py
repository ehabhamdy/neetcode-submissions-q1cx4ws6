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

        while len(stack)>0:
            ch, ci = stack.pop()
            area = ch * (len(heights) - ci)
            res = max(res, area)

        return res