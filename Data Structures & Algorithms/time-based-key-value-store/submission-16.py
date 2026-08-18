class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.store:
        #     self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        n = len(values)
        l, r = 0, n - 1
        res = -1
        while l <= r:
            m = l + ((r - l) // 2)
            midTimestamp = values[m][0]
            if midTimestamp > timestamp:
                r = m - 1
            elif midTimestamp < timestamp:
                l = m + 1
                res = m
            else:
                return values[m][1]
        return "" if res == -1 else values[res][1]
            