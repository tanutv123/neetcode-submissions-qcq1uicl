class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visit = set()
        def dfs(root, parr):
            if root in visit:
                return False
            
            visit.add(root)
            for nei in adj[root]:
                if nei == parr:
                    continue
                if not dfs(nei, root):
                    return False
            
            return True
        return dfs(0, 0) and len(visit) == n
