class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0

        def dfs(r, c):
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            total = 1
            grid[r][c] = 0
            for dr, dc in directions:
                total += dfs(r + dr, c + dc)
            return total
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res