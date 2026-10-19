class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) > len(self.right):
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        if self.right and self.right[0] < -self.left[0]:
            l, r = heapq.heappop(self.left), heapq.heappop(self.right)
            heapq.heappush(self.left, -r)
            heapq.heappush(self.right, -l)

    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2:
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2
        