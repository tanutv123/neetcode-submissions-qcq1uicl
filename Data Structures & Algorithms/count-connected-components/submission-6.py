class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = [False] * n
        adj = {i: [] for i in range(n)}

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        def dfs(node):
            for nei in adj[node]:
                if visit[nei]:
                    continue
                visit[nei] = True
                dfs(nei)
        res = 0
        for v in range(n):
            if not visit[v]:
                visit[v] = True
                dfs(v)
                res += 1
        return res
                