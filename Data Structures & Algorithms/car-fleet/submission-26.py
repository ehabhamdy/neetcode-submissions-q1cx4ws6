class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []
        for p, s in cars[::-1]:
            ttd = (target-p)/s 
            stack.append(ttd)

            if len(stack) > 1 and ttd <= stack[-2]:
                stack.pop()

            

        return len(stack)

