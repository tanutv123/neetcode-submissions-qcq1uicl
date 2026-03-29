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
            
            if adj[src] == []:
                return False
            
            for i, dst in enumerate(adj[src]):
                adj[src].pop(i)
                res.append(dst)
                if dfs(dst):
                    return True
                
                adj[src].insert(i, dst)
                res.pop()
            
            return False
        
        dfs("JFK")
        return res 
