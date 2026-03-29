class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        def dfs(r, c, curr):
            if curr == word:
                return True
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit:
                return False
        
            visit.add((r, c))
            curr += board[r][c]
            res = (dfs(r + 1, c, curr) 
                    or dfs(r - 1, c, curr) 
                    or dfs(r, c + 1, curr) 
                    or dfs(r, c - 1, curr))
            visit.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, ""):
                    return True
        return False