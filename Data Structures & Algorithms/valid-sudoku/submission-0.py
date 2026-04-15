from collections import defaultdict
import math

class Solution:
    def containDuplicate(self, strs: List[str]):
        
        s_set = set()
        for s in strs:
            if s in s_set:
                return True
            
            if s != "." and s != ",":
                s_set.add(s)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if self.containDuplicate(board[i]):
                return False
            
            col = []
            for j in range(len(board[i])):
                col.append(board[j][i])

            if self.containDuplicate(col):
                return False

        squares = defaultdict(list)
        for row in range(len(board)):
            for col in range(len(board)):
                # check if square_idx changed
                square_idx = math.floor(row / 3) * 3 + math.floor(col / 3)
                if board[row][col] != "." and board[row][col] != ",":
                    squares[square_idx].append(board[row][col])

        print(dict(squares))
        for k, v in squares.items():
            if self.containDuplicate(v):
                return False

        return True