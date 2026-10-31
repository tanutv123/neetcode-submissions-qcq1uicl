class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = defaultdict(list)
        for v1, v2 in edges:
            edgeMap[v1].append(v2)
            edgeMap[v2].append(v1)

        cycle = set()
        def dfs(i, parent):
            if i in cycle:
                return False
            
            cycle.add(i)
            for e in edgeMap[i]:
                if e == parent:
                    continue
                if not dfs(e, i):
                    return False
            return True
        
        return dfs(0, -1) and len(cycle) == n