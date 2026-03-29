class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
            while prices[l] > prices[r]:
                l += 1
            r += 1
        return maxP
