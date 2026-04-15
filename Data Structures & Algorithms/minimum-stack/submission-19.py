class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        currMin = self.stackMin[-1] if self.stackMin and self.stackMin[-1] < val else val
        self.stackMin.append(currMin)


    def pop(self) -> None:
        self.stack.pop()
        self.stackMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]
        
