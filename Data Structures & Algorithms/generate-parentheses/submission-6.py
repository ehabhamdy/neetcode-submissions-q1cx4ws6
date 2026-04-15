class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []

        def dfs(op, cl):
            if op == n and cl == n:
                res.append("".join(sub))
                return 

            if op < n:
                sub.append('(')
                dfs(op+1, cl)
                sub.pop()

            if cl < op:
                sub.append(')')
                dfs(op, cl+1)
                sub.pop()

        dfs(0, 0)

        return res