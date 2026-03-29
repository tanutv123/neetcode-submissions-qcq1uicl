class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        time = 0
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                cnt, index = q.popleft()
                heapq.heappush(maxHeap, cnt)
        return time