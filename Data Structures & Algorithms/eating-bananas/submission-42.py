class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            m = l + ((r - l) // 2)
            time = 0
            for p in piles:
                time += math.ceil(p / m)
            if time > h:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res
