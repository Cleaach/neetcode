class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        def help(i, j):
            if i >= m or j >= n:
                return 0
            if dp[i][j] == -1:
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + help(i + 1, j + 1)
                else:
                    dp[i][j] = max(help(i + 1, j), help(i, j + 1))
            return dp[i][j]
        
        res = help(0, 0)
        print(dp)
        return res