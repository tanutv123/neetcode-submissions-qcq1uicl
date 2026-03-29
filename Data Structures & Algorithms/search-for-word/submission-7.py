class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        flag = False

        def dfs(r, c, target):
            nonlocal flag
            if min(r, c) < 0 or (r, c) in visit or r >= ROWS or c >= COLS or flag:
                return
            
            visit.add((r, c))
            target += board[r][c]
            if target == word:
                flag = True
                return
            dfs(r + 1, c, target)
            dfs(r - 1, c, target)
            dfs(r, c + 1, target)
            dfs(r, c - 1, target)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "")
        
        return flag