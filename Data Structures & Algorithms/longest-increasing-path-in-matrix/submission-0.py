class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def help(i, j):
            if dp[i][j] == -1:
                res = 1
                for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    if 0 <= i + dx < m and 0 <= j + dy < n and matrix[i + dx][j + dy] > matrix[i][j]:
                        res = max(res, 1 + help(i + dx, j + dy))
                dp[i][j] = res
            return dp[i][j]
        
        r = 0
        for i in range(m):
            for j in range(n):
                r = max(r, help(i, j))

        print(dp)

        return r