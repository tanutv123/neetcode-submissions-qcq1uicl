class DSU:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = list(range(n + 1))
    
    def find(self, i):
        curr = self.parent[i]
        while curr != self.parent[curr]:
            curr = self.parent[self.parent[curr]]
        return curr
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = DSU(len(edges))
        for v1, v2 in edges:
            if not root.union(v1, v2):
                return [v1, v2]
        return []
        