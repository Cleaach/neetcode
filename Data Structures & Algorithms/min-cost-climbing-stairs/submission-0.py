class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for _ in range(len(cost) + 1)]

        # helper function, min cost to reach step n
        def help(n):
            if n < 2:
                return 0
            if dp[n] == -1:
                # min cost to reach n is min cost to reach n - 1 + cost[n - 1] and that of n - 2
                dp[n] = min(help(n - 1) + cost[n - 1], help(n - 2) + cost[n - 2])
            return dp[n]
        
        # need: min cost to reach step n
        return help(len(cost))