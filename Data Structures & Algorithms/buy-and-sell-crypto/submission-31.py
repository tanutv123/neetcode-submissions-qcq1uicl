class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) <= 1):
            return 0
        res = 0
        l = 0
        r = 1
        while (r < len(prices)):
            res = max(prices[r] - prices[l], res)
            if (prices[l] >= prices[r]):
                l = r
            r+= 1
        return res

                