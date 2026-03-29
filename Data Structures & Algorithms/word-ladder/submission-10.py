class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord):
            return False
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "#" + word[i+1:]
                adj[pattern].append(word)
        

        visit = set()
        q = deque()
        visit.add(beginWord)
        q.append(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "#" + word[i+1:]
                    for w in adj[pattern]:
                        if w not in visit:
                            q.append(w)
                            visit.add(w)
            res += 1
        return 0
        