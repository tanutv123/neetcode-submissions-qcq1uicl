class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for s, d, w in times:
            edges[s].append((d, w))
        
        minHeap = [(0, k)]
        visit = {}
        res = 0
        while minHeap:
            w, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            
            visit[n1] = w
            res = w
            for d, w1 in edges[n1]:
                if d in visit:
                    continue
                heapq.heappush(minHeap, (w1 + w, d))
        
        return res if len(visit) == n else -1
