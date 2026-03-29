class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        visit = [False] * n
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res += 1
        return res