class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        pac, alt = set(), set()

        def dfs(r, c, visit, prevHeight):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] < prevHeight:
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, grid[r][c])
            dfs(r - 1, c, visit, grid[r][c])
            dfs(r, c + 1, visit, grid[r][c])
            dfs(r, c - 1, visit, grid[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, grid[0][c])
            dfs(ROWS - 1, c, alt, grid[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, grid[r][0])
            dfs(r, COLS - 1, alt, grid[r][COLS - 1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])
        return res