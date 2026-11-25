class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: [] for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        res = []
        cycle = set()
        visit = set()
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            cycle.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True
        for c in adj.keys():
            if not dfs(c):
                return ""
        return "".join(res[::-1])