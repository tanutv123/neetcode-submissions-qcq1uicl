class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = collections.defaultdict(list)

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        visit = set()
        minHeap = [(0, 0)]
        res = 0
        while minHeap:
            dist, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            visit.add(point)
            res += dist
            for neiDist, nei in adj[point]:
                if nei in visit:
                    continue
                heapq.heappush(minHeap, (neiDist, nei))
        
        return res