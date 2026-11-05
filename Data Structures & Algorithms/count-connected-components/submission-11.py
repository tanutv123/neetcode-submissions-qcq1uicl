class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = defaultdict(list)
        for v1, v2 in edges:
            edgeMap[v1].append(v2)
            edgeMap[v2].append(v1)
        visit = set()
        def dfs(i, parr):
            if i in visit:
                return
            visit.add(i)
            for v in edgeMap[i]:
                if v == parr:
                    continue
                dfs(v, i)
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                res += 1
        return res