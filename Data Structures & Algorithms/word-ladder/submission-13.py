class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        store = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                store[self.getPattern(word, i)].append(word)
        q = deque([beginWord])
        visit = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for w in store[self.getPattern(word, i)]:
                        if w in visit:
                            continue
                        q.append(w)
                        visit.add(w)
            res += 1
        return 0
    
    def getPattern(self, word, index):
        return word[:index] + "*" + word[index+1:]