from collections import deque
import operator 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda op1, op2: int(op1 / op2)
        }

        stack = deque()

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                # get the last two elements, apply the operator, pop the elements and remove 
                op_function = operators.get(token)
                operand2, operand1 = stack.pop(), stack.pop()
                

                stack.append(op_function(operand1, operand2))

        return stack[0]