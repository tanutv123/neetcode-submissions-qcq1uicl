class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        pacific = atlantic = False

        def dfs(r, c, prev):
            nonlocal pacific, atlantic
            if r < 0 or c < 0:
                pacific = True
                return

            if r >= ROWS or c >= COLS:
                atlantic = True
                return

            if grid[r][c] > prev:
                return
            
            tmp = grid[r][c]
            grid[r][c] = float('inf')
            for dr, dc in directions:
                dfs(r + dr, c + dc, tmp)
                if pacific and atlantic:
                    break
            grid[r][c] = tmp
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                pacific = False
                atlantic = False
                dfs(r, c, float('inf'))
                if pacific and atlantic:
                    res.append([r, c])
        return res
