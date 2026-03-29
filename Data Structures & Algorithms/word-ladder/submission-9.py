class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "#" + word[i+1:]
                adj[pattern].append(word)
        

        q = deque([beginWord])
        visit = set()
        visit.add(beginWord)
        res = 1
        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "#" + word[i+1:]
                    for w in adj[pattern]:
                        if w in visit:
                            continue
                        q.append(w)
                        visit.add(w)
            res += 1
        return 0