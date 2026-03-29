class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        coins.sort()
        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if (i, a) in dp:
                return dp[(i, a)]
            
            res = 0
            if a >= coins[i]:
                res = dfs(i + 1, a)
                res += dfs(i, a - coins[i])
            dp[(i, a)] = res
            return dp[(i, a)]
        
        return dfs(0, amount)
