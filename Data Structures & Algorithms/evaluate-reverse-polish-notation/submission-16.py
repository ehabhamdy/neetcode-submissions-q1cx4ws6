import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a,b: int(a / b)
        }      

        stack = []

        for t in tokens:
            if t in operators:
                operand1 = stack.pop()
                operand2 = stack.pop()
        
                stack.append(operators[t](operand2, operand1))

            else:
                stack.append(int(t))


        return stack[0]