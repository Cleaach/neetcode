class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for p in list(self.points.keys())[:]:
            if abs(p[0] - point[0]) == abs(p[1] - point[1]) != 0: # diagonal
                res += self.points[p] * self.points[tuple([point[0], p[1]])] * self.points[tuple([p[0], point[1]])]
        return res
