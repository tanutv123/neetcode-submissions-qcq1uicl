class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0],0,0)]
        res = 0
        visit = [[False] * n for _ in range(n)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if visit[r][c]:
                continue
            if r == n - 1 and c == n - 1:
                return t
            visit[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or max(nr, nc) >= n or visit[nr][nc]:
                    continue
                heapq.heappush(minHeap, (max(t, grid[nr][nc]), nr, nc))
        