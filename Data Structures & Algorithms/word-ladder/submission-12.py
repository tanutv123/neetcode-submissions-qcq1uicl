class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        
        res = 1
        visit = set()
        visit.add(beginWord)
        q = deque([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neig in nei[pattern]:
                        if neig not in visit:
                            q.append(neig)
                            visit.add(neig)
            res += 1
        return 0


