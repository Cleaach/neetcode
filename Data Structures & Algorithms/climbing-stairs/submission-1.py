class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [-1 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2

        def help(n):
            if dp[n] == -1:
                dp[n] = help(n - 1) + help(n - 2)
            return dp[n]
        
        return help(n - 1)