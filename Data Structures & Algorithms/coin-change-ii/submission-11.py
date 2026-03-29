class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1   
            for a in range(1, amount + 1):
                if a - coins[i] >= 0:
                    nextDp[a] = nextDp[a - coins[i]] + dp[a]
            dp = nextDp
        return dp[-1]