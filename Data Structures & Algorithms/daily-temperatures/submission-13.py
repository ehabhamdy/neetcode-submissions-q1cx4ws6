class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < t:
                (it, tt) = stack.pop()
                res[it] = i - it

            stack.append((i, t))

        return res