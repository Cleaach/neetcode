class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        limit = -1
        for interval in intervals:
            limit = max(limit, interval[1])
        
        arr = [-1] * (max(max(queries), limit) + 1)

        for x, y in intervals:
            l = y - x + 1
            for i in range(x, y + 1):
                if arr[i] == -1:
                    arr[i] = l
                else:
                    arr[i] = min(arr[i], l)
        
        res = []
        for query in queries:
            res.append(arr[query])
        
        return res