class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = defaultdict(list)
        for v1, v2 in edges:
            edgeMap[v1].append(v2)
            edgeMap[v2].append(v1)
        
        visit = set()
        def dfs(i, par):
            if i in visit:
                return False
            visit.add(i)
            for nei in edgeMap[i]:
                if nei == par:
                    continue
                if not dfs(nei, i):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n