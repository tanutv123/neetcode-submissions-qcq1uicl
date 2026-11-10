class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edgeMap = defaultdict(list)
        for u, v, t in times:
            edgeMap[u].append([v, t])
        minHeap = [[0, k]]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            t = w1
            visit.add(n1)
            for v, w in edgeMap[n1]:
                if v not in visit:
                    heapq.heappush(minHeap, [w1 + w, v])
        return t if len(visit) == n else -1