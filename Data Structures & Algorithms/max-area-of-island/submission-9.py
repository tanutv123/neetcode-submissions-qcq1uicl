class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0

        def dfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 1
            while q:
                row, col = q.pop()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1
            return area

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res
