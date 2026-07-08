class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        q = [] # (max height in path, x, y)
        heapq.heapify(q)
        heapq.heappush(q, (grid[0][0], 0, 0))
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n = len(grid)
        seen = set() # elements are (x, y)
        while q:
            m, x, y = heapq.heappop(q)
            if x == n - 1 and y == n - 1:
                return m
            if (x, y) in seen:
                continue
            seen.add((x, y))
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    heapq.heappush(q, (max(grid[nx][ny], m), nx, ny))
        return "WOW"
