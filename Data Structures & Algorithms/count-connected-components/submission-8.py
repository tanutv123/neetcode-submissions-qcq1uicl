class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visit = set()

        def dfs(node):
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)

        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res