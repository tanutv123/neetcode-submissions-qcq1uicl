class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        adj = collections.defaultdict(list)
        for s, d, w in flights:
            adj[s].append((d, w))
        
        q = [(0, src, -1)]
        while q:
            w, node, stops = heapq.heappop(q)
            if stops > k:
                continue
            
            prices[node] = min(prices[node], w)
            for nei, c in adj[node]:
                heapq.heappush(q, (w + c, nei, stops + 1))
        
        return prices[dst] if prices[dst] != float('inf') else -1