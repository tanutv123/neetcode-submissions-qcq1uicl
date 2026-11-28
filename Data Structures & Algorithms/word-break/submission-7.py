class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict = defaultdict(list)
        for w in wordDict:
            dict[w[0]].append(w)
        failed = set()
        def dfs(i):
            if i >= len(s):
                return True
            if i in failed:
                return False
            for w in dict[s[i]]:
                if s[i:i+len(w)] == w and dfs(i + len(w)):
                    return True
            failed.add(i)
            return False
        return dfs(0)
        
