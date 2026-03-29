class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        # prices[src] = 0
        adj = collections.defaultdict(list)
        for s, d, c in flights:
            adj[s].append([d, c])
        
        q = deque([(0, src, -1)])
        while q:
            oldCost, node, stops = q.popleft()
            
            if stops > k:
                continue
            
            prices[node] = min(prices[node], oldCost)

            for nei, w in adj[node]:
                newCost = w + oldCost
                q.append((newCost, nei, stops + 1))
        
        return prices[dst] if prices[dst] != float('inf') else -1
