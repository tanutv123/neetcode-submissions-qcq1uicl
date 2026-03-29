class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if not adj[src]:
                return False
            
            tmp = list(adj[src])
            for i, v in enumerate(adj[src]):
                res.append(v)
                adj[src].pop(i)

                if dfs(v):
                    return True
                
                res.pop()
                adj[src].insert(i, v)
        dfs("JFK")
        return res