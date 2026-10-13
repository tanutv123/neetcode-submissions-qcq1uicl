class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) > len(self.right):
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        if self.right and -self.left[0] > self.right[0]:
            numLeft = -heapq.heappop(self.left)
            numRight = heapq.heappop(self.right)
            heapq.heappush(self.left, -numRight)
            heapq.heappush(self.right, numLeft)


    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2:
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2        
        