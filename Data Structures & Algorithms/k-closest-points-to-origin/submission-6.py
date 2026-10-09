class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(maxHeap, [-dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res