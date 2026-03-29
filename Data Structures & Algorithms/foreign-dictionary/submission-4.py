class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(len(w1)):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = set()
        cycle = set()
        res = []

        def dfs(c):
            if c in cycle:
                return True
            if c in visit:
                return False
            
            cycle.add(c)
            for nei in adj[c]:
                if dfs(nei):
                    return True
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return False
        for c in adj:
            if c not in visit:
                if dfs(c):
                    return ""
        res.reverse()
        return "".join(res)
            