class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ss, tt = len(s), len(t)
        dp = [[-1 for _ in range(tt)] for _ in range(ss)]
        def help(i, j):
            if i == ss and j == tt:
                return 1
            if i == ss:
                return 0
            if j == tt:
                return 1
            if dp[i][j] == -1:
                if s[i] == t[j]:
                    dp[i][j] = help(i + 1, j + 1) + help(i + 1, j)
                else:
                    dp[i][j] = help(i + 1, j)
            return dp[i][j]
        return help(0, 0)
