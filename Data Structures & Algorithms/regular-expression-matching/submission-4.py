class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)
        def dfs(i, j):
            if i >= n1 and j >= n2:
                return True

            if j >= n2:
                return False
            
            matching =  i < n1 and (s[i] == p[j] or p[j] == '.')
            if (j + 1 < n2 and p[j + 1] == '*'):
                return (dfs(i, j + 2) or
                       (matching and dfs(i + 1, j)))
            if matching:
                return dfs(i + 1, j + 1)
            
            return False
        
        return dfs(0, 0)


"""

s = aab
p = a*bc

"""