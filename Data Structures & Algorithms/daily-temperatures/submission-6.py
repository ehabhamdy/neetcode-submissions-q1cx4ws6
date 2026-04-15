class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # decremental monotonic stacks
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                st, si = stack.pop()
                res[si] = i - si

            stack.append((t, i))

        return res