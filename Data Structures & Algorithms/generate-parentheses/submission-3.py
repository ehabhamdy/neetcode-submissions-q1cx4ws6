class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        exp = []
        def backtrack(nopen, nclose):
            print(nopen)
            print(nclose)
            if nopen == nclose == n:
                print('yes', exp)
                res.append(''.join(exp))
                return

            if nopen < n or nclose == nopen:
                exp.append('(')
                backtrack(nopen+1, nclose)
                exp.pop()
            
            if nclose < nopen:
                exp.append(')')
                backtrack(nopen, nclose+1)
                exp.pop()

        backtrack(0, 0)

        return res