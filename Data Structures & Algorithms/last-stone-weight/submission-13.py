class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1, stone2 = heapq.heappop(max_heap), heapq.heappop(max_heap)
            remains = abs(stone1 - stone2)
            if remains:
                heapq.heappush(max_heap, -1 * remains)
        
        return abs(max_heap[0]) if max_heap else 0
