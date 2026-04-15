class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []
        # fleets = 0
        for i in range(len(position)-1, -1, -1):
            if len(stack) == 0:
                stack.append(cars[i])
                continue
            # if the stack is not empty then calculate the time to distination
            # for the new element and the 
            car1TimeToD = (target-stack[-1][0])/stack[-1][1]
            car2TimeToD = (target-cars[i][0])/cars[i][1]
            print(car1TimeToD)
            print(car2TimeToD)
            if car2TimeToD > car1TimeToD:
                print('damm')
                stack.append(cars[i])
            
        return len(stack)
        
