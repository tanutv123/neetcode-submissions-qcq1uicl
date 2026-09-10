class TimeMap:

    def __init__(self):
        self.store = {} # key: [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        value = self.store[key]
        l, r = 0, len(value) - 1
        res = ""
        while l <= r:
            m = l + ((r - l) // 2)
            t = value[m][0]
            if t > timestamp:
                r = m - 1
            else:
                l = m + 1
                res = value[m][1]
        return res
