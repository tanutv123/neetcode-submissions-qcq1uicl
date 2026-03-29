class TimeMap:

    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        totalLen = len(self.store[key])
        res = ""
        l, r = 0, totalLen - 1
        while l <= r:
            m = (l + r) // 2
            if self.store[key][m][1] <= timestamp:
                res = self.store[key][m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
