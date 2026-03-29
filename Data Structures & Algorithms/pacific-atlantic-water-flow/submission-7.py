class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        pac, alt = set(), set()

        def dfs(r, c, prev, visit):
            if (r, c) in visit or r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] < prev:
                return
            
            visit.add((r, c))
            dfs(r + 1, c, grid[r][c], visit)
            dfs(r - 1, c, grid[r][c], visit)
            dfs(r, c + 1, grid[r][c], visit)
            dfs(r, c - 1, grid[r][c], visit)

        for c in range(COLS):
            dfs(0, c, grid[0][c], pac)
            dfs(ROWS - 1, c, grid[ROWS - 1][c], alt)
        
        for r in range(ROWS):
            dfs(r, 0, grid[r][0], pac)
            dfs(r, COLS - 1, grid[r][COLS - 1], alt)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in alt:
                    res.append((r, c))
        return res