class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        n = len(interval)
        interval.sort()
        j = 0
        res= []
        while j < n:
            i = j + 1
            newInterval = interval[j]
            while i < n and newInterval[1] >= interval[i][0]:
                newInterval[0] = min(newInterval[0], interval[i][0])
                newInterval[1] = max(newInterval[1], interval[i][1])
                i += 1
            res.append(newInterval)
            j = i
        return res