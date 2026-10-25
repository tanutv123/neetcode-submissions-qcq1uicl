class TimeMap:

    def __init__(self):
        self.store = {} #key: [[timestamp1, value1], [timestamp2, value2]]


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        data = self.store[key]
        l, r = 0, len(data) - 1
        res = ""
        while l <= r:
            m = l + ((r - l) // 2)

            if data[m][0] > timestamp:
                r = m - 1
            else:
                res = data[m][1]
                l = m + 1
        return res
