class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        
        adj = {i: [] for i in range(n)}
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        q = deque()
        q.append((0, -1))
        visit = set()
        visit.add(0)

        while q:
            curr, par = q.popleft()
            for nei in adj[curr]:
                if nei == par:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, curr))
        return len(visit) == n