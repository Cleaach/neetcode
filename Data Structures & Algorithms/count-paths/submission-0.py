class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = 1
        def help(i, j):
            if i >= m or j >= n:
                return 0
            if dp[i][j] == -1:
                dp[i][j] = help(i + 1, j) + help(i, j + 1)
            return dp[i][j]
        return help(0, 0)