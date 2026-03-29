class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS = len(matrix[0])
        ROWS = len(matrix)

        top = 0
        bot = ROWS - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
