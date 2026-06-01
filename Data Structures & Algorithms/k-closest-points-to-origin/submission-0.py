class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(l):
            return (l[0] ** 2 + l[1] ** 2) ** 0.5
        arr = []
        heapq.heapify(arr)
        for point in points:
            heapq.heappush(arr, (dist(point), point))
        res = []
        for i in range(k):
            d, point = heapq.heappop(arr)
            res.append(point)
        return res