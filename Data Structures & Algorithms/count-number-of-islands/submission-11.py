class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0':
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    bfs(r, c)
        return res