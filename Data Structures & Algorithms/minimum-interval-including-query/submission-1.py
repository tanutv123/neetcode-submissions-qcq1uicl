class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []

        for q in queries:
            curr = -1
            for l, r in intervals:
                if (l <= q <= r and (curr == -1 or r - l + 1 < curr)):
                    curr = r - l + 1
            res.append(curr)
        return res