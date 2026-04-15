import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand2 - operand1)
            elif t == "/":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(int(operand2 / operand1))
            else:
                stack.append(int(t))

        

        return stack[0]
