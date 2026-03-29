class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for s, d, w in times:
            adj[s].append((d, w))
        
        shortest = {}
        res = 0
        minHeap = [(0, k)]
        while minHeap:
            w, d = heapq.heappop(minHeap)
            if d in shortest:
                continue
            shortest[d] = w
            res = w
            for d1, w1 in adj[d]:
                if d1 in shortest:
                    continue
                heapq.heappush(minHeap, (w1 + w, d1))


        return res if len(shortest) == n else -1