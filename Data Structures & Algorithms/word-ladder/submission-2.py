class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj[pattern].append(word)
        
        visit = set()
        q = deque([beginWord])
        visit.add(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adj[pattern]:
                        if nei in visit:
                            continue
                        q.append(nei)
                        visit.add(nei)
            res += 1
        return 0