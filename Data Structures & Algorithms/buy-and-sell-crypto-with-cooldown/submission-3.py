class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0

            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, False) - prices[i]
                return max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, buying)
                return max(sell, cooldown)
        
        return dfs(0, True)
