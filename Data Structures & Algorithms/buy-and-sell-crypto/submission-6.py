class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1
        maxProfit = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)

            while prices[r] < prices[l]:
                l = r
            r += 1
        return maxProfit