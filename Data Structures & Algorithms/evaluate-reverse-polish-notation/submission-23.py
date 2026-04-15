class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop()+stack.pop())
            elif t == '*':
                stack.append(stack.pop()*stack.pop())
            elif t == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2-op1)
            elif t == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2/op1))  
            else:
                stack.append(int(t))

        return stack[-1]
