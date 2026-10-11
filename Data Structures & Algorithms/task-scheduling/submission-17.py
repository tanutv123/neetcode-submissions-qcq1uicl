class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        for task in tasks:
            cnt[ord(task) - ord('A')] += 1
        
        maxHeap = []
        for f in cnt:
            if f > 0:
                heapq.heappush(maxHeap, -f)
            
        time = 0
        q = deque() #[-cnt, wait]

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time
