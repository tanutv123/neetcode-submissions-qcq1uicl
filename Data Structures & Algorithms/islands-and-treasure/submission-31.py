class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            visit = set([(r, c)])
            dist = 1
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit or grid[nr][nc] == -1:
                            continue
                        if grid[nr][nc] == 0:
                            return dist
                        q.append((nr, nc))
                        visit.add((nr, nc))
                dist += 1
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        
                        