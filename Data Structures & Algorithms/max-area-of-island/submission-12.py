class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append([r, c])
            total = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if min(nc, nr) < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                        continue
                    total += 1
                    grid[nr][nc] = 0
                    q.append([nr, nc])
            return total
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res
