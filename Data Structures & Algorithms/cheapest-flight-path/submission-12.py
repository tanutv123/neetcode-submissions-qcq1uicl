class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        adj = collections.defaultdict(list)
        for s, d, w in flights:
            adj[s].append([d, w])

        q = deque([(0, src, -1)])

        while q:
            w, node, stops = q.popleft()
            if stops > k:
                continue
            
            prices[node] = min(w, prices[node])

            for d, c in adj[node]:
                q.append((w + c, d, stops + 1))
        
        return prices[dst] if prices[dst] != float('inf') else -1