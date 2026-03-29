class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adjList = [[] for i in range(n)]

        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        visit = set()
        def dfs(node, parrent):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adjList[node]:
                if nei == parrent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n