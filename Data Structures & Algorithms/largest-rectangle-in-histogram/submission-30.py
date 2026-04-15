class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            index = i
            while stack and h < stack[-1][1]:
                ii, hh = stack.pop()
                res = max(res, (i-ii)*hh)
                index = ii

            stack.append((index, h))

        # remaining elements where the can be extended from their position i to the end of the stack len(stack)
        for i, h in stack:
            res = max(res, (len(heights)-i)*h)

        
        return res