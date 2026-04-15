class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stackMin:
            currMin = val if val < self.stackMin[-1] else self.stackMin[-1]
        else:
            currMin = val
        self.stackMin.append(currMin)


    def pop(self) -> None:
        self.stack.pop()
        self.stackMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]
        
