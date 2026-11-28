class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        par = [i for i in range(n)]
        def find(i):
            res = par[i]
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(p1, p2):
            n1, n2 = find(p1), find(p2)
            if n1 == n2:
                return 0
            if rank[n1] > rank[n2]:
                par[n2] = n1
                rank[n1] += 1
            else:
                par[n1] = n2
                rank[n2] += 1
            return 1
        res = n
        for v1, v2 in edges:
            res -= union(v1, v2)
        return res
            