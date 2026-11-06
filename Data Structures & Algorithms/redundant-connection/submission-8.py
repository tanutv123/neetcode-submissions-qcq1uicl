class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        res = []
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            nonlocal res
            if p1 == p2:
                res = [n1, n2]
                return
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] += 1
            return
        for v1, v2 in edges:
            union(v1, v2)
        return res