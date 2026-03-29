class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        def dfs(i, j):
            if i == n1:
                return len(word2) - j
            if j == n2:
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            insert = 1 + dfs(i, j + 1)
            delete = 1 + dfs(i + 1, j)
            replace = 1 + dfs(i + 1, j + 1)
            return min(insert, delete, replace)
        
        return dfs(0,0)