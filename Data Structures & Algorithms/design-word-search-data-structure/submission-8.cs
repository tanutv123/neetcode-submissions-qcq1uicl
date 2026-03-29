public class TrieNode {
    public Dictionary<char, TrieNode> children {get; set;} = new Dictionary<char, TrieNode>();
    public bool word {get; set;} = false;
}
public class WordDictionary {
    private TrieNode root;
    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void AddWord(string word) {
        var curr = root;
        foreach(var c in word) {
            if(!curr.children.ContainsKey(c)) {
                curr.children[c] = new TrieNode();
            }
            curr = curr.children[c];
        }
        curr.word = true;
    }
    
    public bool Search(string word) {
        return Dfs(0, root, word);
    }

    private bool Dfs(int j, TrieNode root, string word) {
        var curr = root;
        for(int i = j; i < word.Length; i++) {
            var c = word[i];
            if(c == '.') {
                foreach(var child in curr.children.Values) {
                    if(Dfs(i + 1, child, word)) {
                        return true;
                    }
                }
                return false;
            } else {
                if(!curr.children.ContainsKey(c)) {
                    return false;
                }
                curr = curr.children[c];
            }
        }
        return curr.word;
    }
}
