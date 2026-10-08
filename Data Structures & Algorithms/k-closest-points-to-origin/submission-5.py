class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for i in range(len(points)):
            distance = -(points[i][0] ** 2 + points[i][1] ** 2)
            heapq.heappush(maxHeap, [distance, points[i]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res