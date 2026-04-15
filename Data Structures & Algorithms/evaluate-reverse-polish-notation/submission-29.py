class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(stack)
            print(t)
            if t.lstrip('-').isdigit():
                stack.append(int(t))
                continue
            
            operand1 = stack.pop()
            operand2 = stack.pop()

            if t == "+":
                stack.append(operand1 + operand2)
            elif t == "*":
                stack.append(operand1 * operand2)
            elif t == "-":
                stack.append(operand2 - operand1)
            else:
                stack.append(int(operand2 / operand1))
            
        return stack[0]
            
