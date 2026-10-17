class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for c in tasks:
            count[ord(c) - ord('A')] += 1
        maxHeap = []
        for c in count:
            if c == 0:
                continue
            heapq.heappush(maxHeap, -c)
        
        q = deque() #[-cnt, time to wait]
        time = 0
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxHeap)
                cnt = cnt + 1
                if cnt != 0:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time