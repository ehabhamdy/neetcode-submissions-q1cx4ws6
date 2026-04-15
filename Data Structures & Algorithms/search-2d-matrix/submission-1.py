class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        RAWS, COLS = len(matrix), len(matrix[0])
        t, b = 0, RAWS-1
        
        row = 0
        while t <= b:
            row = t + (b - t) //2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break

        if not (t <= b):
            return False

        l, r = 0, COLS-1
        m = 0 
        while l <= r:
            m = l + (r-l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = r - 1
            else:
                return True

        return False
        