class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            while len(monoStack)!=0 and monoStack[-1][0] <= temperatures[i]:
                monoStack.pop()

            if len(monoStack) == 0: 
                res[i] = 0
            else:
                res[i] = monoStack[-1][1] - i
            
            monoStack.append((temperatures[i], i))

        return res