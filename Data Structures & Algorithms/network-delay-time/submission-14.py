class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i: [] for i in range(1, n + 1)}
        for s, d, w in times:
            edges[s].append((d, w))
        
        minHeap = [(0, k)]
        visit = {}
        res = 0
        while minHeap:
            w, d = heapq.heappop(minHeap)
            if d in visit:
                continue
            visit[d] = w
            res = w
            for d1, w1 in edges[d]:
                if d1 in visit:
                    continue
                heapq.heappush(minHeap, (w1 + w, d1))
        
        return res if len(visit) == n else -1
