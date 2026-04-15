class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.lstrip('-').isdigit():
                stack.append(int(t))
                continue
            
            op1 = stack.pop()
            op2 = stack.pop()
            if t == "*":    
                stack.append(op1 * op2)
            elif t == "+":
                stack.append(op1 + op2)
            elif t == '-':
                stack.append(op2 - op1)
            elif t == '/':
                stack.append(int(op2/op1))
    
        return stack[0]