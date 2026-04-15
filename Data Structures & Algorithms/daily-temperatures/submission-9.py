class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # ind = i
            while monoStack and t > monoStack[-1][0]:
                tt, ti = monoStack.pop()
                # ind = ti
                res[ti] = i - ti

            monoStack.append((t, i))
        
        return res