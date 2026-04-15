class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                ii, tt = stack.pop()
                res[ii] = i - ii
            
            stack.append((i, t))

        return res

