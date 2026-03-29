class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visit = set()
        def dfs(curr, parr):
            if curr in visit:
                return False
            
            visit.add(curr)
            for nei in adj[curr]:
                if nei == parr:
                    continue
                
                if not dfs(nei, curr):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        
