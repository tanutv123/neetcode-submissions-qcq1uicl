class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False

        adj = {i: [] for i in range(n)}
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False

            if node == par:
                return True

            visit.add(node)
            
            for e in adj[node]:
                if e == par:
                    continue
                if not dfs(e, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n