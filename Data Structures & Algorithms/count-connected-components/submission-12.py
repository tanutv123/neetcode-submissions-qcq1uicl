class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        par = [i for i in range(n)]
        def find(i):
            res = i
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            v1, v2 = find(n1), find(n2)
            if v1 == v2:
                return 0
            
            if rank[v1] > rank[v2]:
                par[v2] = v1
                rank[v2] += 1
            else:
                par[v1] = v2
                rank[v1] += 1
            return 1
        res = n
        for v1, v2 in edges:
            res -= union(v1, v2)
        return res