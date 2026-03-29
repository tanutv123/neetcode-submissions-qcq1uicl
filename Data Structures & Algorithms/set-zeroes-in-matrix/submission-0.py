class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])


        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    q.append((r, c))
        
        for i in range(len(q)):
            r, c = q.popleft()
            for row in range(ROWS):
                matrix[row][c] = 0
            for col in range(COLS):
                matrix[r][col] = 0
        
        