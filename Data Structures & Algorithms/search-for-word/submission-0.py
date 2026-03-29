class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        ROWS, COLS = len(board), len(board[0])
        flag = False
        def dfs(r, c, currWord):
            nonlocal flag
            if min(r,c) < 0 or r == ROWS or c == COLS or (r, c) in visit:
                return
            
            visit.add((r, c))
            currWord += board[r][c]
            if currWord == word:
                flag = True
            
            dfs(r + 1, c, currWord)
            dfs(r - 1, c, currWord)
            dfs(r, c + 1, currWord)
            dfs(r, c - 1, currWord)

            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "")

        return flag
