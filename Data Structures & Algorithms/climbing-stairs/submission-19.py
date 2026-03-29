class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 2)
        def dfs(i):
            if cache[i] != -1:
                return cache[i]

            if i >= n:
                return i == n

            
            
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)