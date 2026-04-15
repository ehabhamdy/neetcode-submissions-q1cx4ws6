class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        
        for i, h in enumerate(heights):
            idx = i
            print(stack)
            while stack and h < stack[-1][1]:
                ii, hh = stack.pop()
                res = max(res, hh * (i-ii))
                idx = ii

            stack.append((idx, h))

        print('=======')
        print(stack)

        for i, h in stack:
            print(i, h)
            res = max(res, h * (len(heights)-i))


        return res
