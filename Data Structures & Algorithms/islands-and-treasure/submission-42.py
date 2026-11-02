class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]] 
        INF = 2147483647
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
        time = 0
        while q:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] != INF:
                        continue
                    q.append([nr, nc])
                    grid[nr][nc] = time 
        