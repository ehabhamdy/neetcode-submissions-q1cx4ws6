class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimum = min(val, self.currMin[-1]) if self.currMin else val
        self.currMin.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.currMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currMin[-1]
