class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            totalTime = 0
            k = l + ((r - l ) // 2)

            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res