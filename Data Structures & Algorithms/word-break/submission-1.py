class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, w):
        curr = self.root
        for c in w:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
    
    def search(self, s, i, j):
        curr = self.root
        for idx in range(i, j + 1):
            if s[idx] not in curr.children:
                return False
            curr = curr.children[s[idx]]
        return curr.word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()

        for w in wordDict:
            trie.add(w)
            
        t = 0
        for w in wordDict:
            t = max(t, len(w))

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            for j in range(i, min(len(s), i + t)):
                if trie.search(s, i, j):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break
        return dp[0]
