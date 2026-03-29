class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordSet = set(words)
        ROWS, COLS = len(board), len(board[0])
        res = set()
        def dfs(r, c, word, visit):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit:
                return
            
            visit.add((r, c))
            word += board[r][c]
            if word in wordSet:
                if word not in res:
                    res.add(word)
            dfs(r + 1, c, word, visit)
            dfs(r - 1, c, word, visit)
            dfs(r, c + 1, word, visit)
            dfs(r, c - 1, word, visit)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                visit = set()
                dfs(r, c, "", visit)
        return list(res)