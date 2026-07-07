class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[None] * (n + 1) for _ in range(m + 1)]

        def dfs(i, j):
            if dp[i][j] is not None:
                return dp[i][j]

            if j == n:
                dp[i][j] = (i == m)
                return dp[i][j]

            match = i < m and (s[i] == p[j] or p[j] == ".")

            if j + 1 < n and p[j + 1] == "*":
                dp[i][j] = (
                    dfs(i, j + 2) or
                    (match and dfs(i + 1, j))
                )
            else:
                dp[i][j] = match and dfs(i + 1, j + 1)

            return dp[i][j]

        return dfs(0, 0)