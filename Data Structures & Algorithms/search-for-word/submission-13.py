class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or word[i] != grid[r][c]:
                return False
            
            visit.add((r, c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            visit.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False