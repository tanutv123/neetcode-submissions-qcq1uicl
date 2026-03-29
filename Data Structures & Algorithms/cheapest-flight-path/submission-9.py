class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, w in flights:
                if prices[s] == float('inf'):
                    continue
                if tmpPrices[d] > w + prices[s]:
                    tmpPrices[d] = w + prices[s]
            prices = tmpPrices
        return prices[dst] if prices[dst] != float('inf') else -1