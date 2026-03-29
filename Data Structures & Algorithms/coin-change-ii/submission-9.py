class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextRow = [0] * (amount + 1)
            nextRow[0] = 1
            for a in range(1, amount + 1):
                nextRow[a] = dp[a]
                if a - coins[i] >= 0:
                    nextRow[a] = nextRow[a - coins[i]] + dp[a]
            dp = nextRow
        
        return dp[amount]

