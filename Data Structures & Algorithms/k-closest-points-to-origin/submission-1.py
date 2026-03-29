class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            dist = -(x*x + y*y)
            heapq.heappush(maxHeap, [dist, x, y])
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res