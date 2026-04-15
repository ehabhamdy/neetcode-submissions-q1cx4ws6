from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for l in range(9):
                if board[r][l] == '.':
                    continue
                
                if board[r][l] in rows[r] or board[r][l] in cols[l] or board[r][l] in box[(r//3, l//3)]:
                    return False

                rows[r].add(board[r][l])
                cols[l].add(board[r][l])
                box[(r//3, l//3)].add(board[r][l])

        return True