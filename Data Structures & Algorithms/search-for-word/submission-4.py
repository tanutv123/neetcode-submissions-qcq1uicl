class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        flag = False
        def dfs(r, c, currStr):
            nonlocal flag
            
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit:
                return

            visit.add((r, c))
            currStr += board[r][c]
            if currStr == word:
                flag = True

            dfs(r + 1, c, currStr)
            dfs(r - 1, c, currStr)
            dfs(r, c + 1, currStr)
            dfs(r, c - 1, currStr)

            visit.remove((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "")
        
        return flag