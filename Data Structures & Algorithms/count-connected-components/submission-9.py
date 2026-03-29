class DSU:
    def __init__(self, n):
        self.comps = n
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
        self.comps -= 1
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
    
    def components(self):
        return self.comps

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root = DSU(n)
        for v1, v2 in edges:
            root.union(v1, v2)
        
        return root.components()
        
