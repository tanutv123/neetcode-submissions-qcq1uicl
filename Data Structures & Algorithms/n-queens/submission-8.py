class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []
        curr = [["."] * n for i in range(n)]

        def dfs(r):
            if r >= n:
                copy = ["".join(row) for row in curr]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                curr[r][c] = "Q"
                cols.add(c)
                posDiag.add((r + c))
                negDiag.add((r - c))
                dfs(r + 1)
                curr[r][c] = "."
                cols.remove(c)
                posDiag.remove((r + c))
                negDiag.remove((r - c))
        
        dfs(0)
        return res