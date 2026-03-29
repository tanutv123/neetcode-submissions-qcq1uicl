class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = deque()

        def rotten(r, c):
            nonlocal fresh
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            q.append((r, c))
            grid[r][c] = 2
            fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                rotten(r + 1, c)
                rotten(r - 1, c)
                rotten(r, c + 1)
                rotten(r, c - 1)

            time += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return time


