class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        INF = 2147483647
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROWS and 0 <= nc < COLS
                    and rooms[nr][nc] == INF
                ):
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))
