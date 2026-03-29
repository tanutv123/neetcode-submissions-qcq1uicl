class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0

        for x, y in self.pts:
            if (abs(x - px) != abs(y - py)) or (x == px and y == py):
                continue
            
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        
        return res
