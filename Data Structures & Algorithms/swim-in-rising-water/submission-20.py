class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows ,cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minHeap = [[grid[0][0], 0, 0]]
        currentMaxTime = 0
        visit = set()
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            currentMaxTime = max(currentMaxTime, time)
            if r == (rows - 1) and c == (cols - 1):
                return currentMaxTime
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr >= rows or nc >= cols or (nr, nc) in visit:
                    continue
                heapq.heappush(minHeap, [grid[nr][nc], nr, nc])
        return 0
            
    