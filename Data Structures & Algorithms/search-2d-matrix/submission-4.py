class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        t, b = 0, ROWS-1

        m=0
        while t <= b:
            m = t + (b-t)//2
            if target > matrix[m][-1]:
                t = m + 1
            elif target < matrix[m][0]:
                b = m - 1
            else:
                break

        targetRow = matrix[m]

        l, r = 0, COLS-1

        while l <= r:
            m = l + (r-l)//2
            if target > targetRow[m]:
                l = m + 1
            elif target < targetRow[m]:
                r = m - 1
            else:
                return True

        return False