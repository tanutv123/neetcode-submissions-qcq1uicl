class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i : [] for i in range(n)}

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        cycle = set()
        visit = set()

        def dfs(node, parr):
            if node in cycle:
                return False
            
            cycle.add(node)
            for nei in adj[node]:
                if nei == parr:
                    continue
                if not dfs(nei, node):
                    return False
            cycle.remove(node)
            visit.add(node)
            return True
        
        return dfs(0, -1) and len(visit) == n