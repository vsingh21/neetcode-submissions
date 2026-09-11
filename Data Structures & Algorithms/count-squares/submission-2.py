class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0
        for (x, y), freq in self.points.items():
            if abs(qx - x) == abs(qy - y) and abs(qx - x) != 0:
                p1 = x, qy
                p2 = qx, y
                if p1 in self.points and p2 in self.points:
                    freq *= self.points[p1]
                    freq *= self.points[p2]
                    res += freq
        return res

        
