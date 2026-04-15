import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # operators = {
        #     '+': operator.add,
        #     '-': operator.subtract,
        #     '*': operator.multiply,
        #     '/': lambda a,b: a // b
        # }      

        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '-':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 - operand2)
            elif t == '/':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(int(float(operand1) / operand2))
            else:
                stack.append(int(t))

        
        return stack[0]