class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, cost in flights:
            adj[s].append([cost, d])
        res = float('inf')
        def dfs(node, acc, remaining):
            nonlocal res
            if acc >= res:
                return
            if node == dst:
                res = min(acc, res)
                return
            if remaining == 0:
                return
            for cost, nei in adj[node]:
                dfs(nei, acc + cost, remaining - 1)
        dfs(src, 0, k + 1)
        return res if res != float('inf') else -1

