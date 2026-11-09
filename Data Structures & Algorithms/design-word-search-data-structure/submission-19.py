class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            if i == len(word):
                return node.end
            c = word[i]
            if c != ".":
                if c not in node.children:
                    return False
                return dfs(i + 1, node.children[c])
            else:
                for child in node.children:
                    if dfs(i + 1, node.children[child]):
                        return True
                return False
            return False
        return dfs(0, self.root)
