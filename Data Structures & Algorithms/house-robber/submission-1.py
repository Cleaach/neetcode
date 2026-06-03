class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # dp[n] is answer for first n + 1 houses
        dp = [-1 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        def help(n):
            if dp[n] == -1:
                dp[n] = max(help(n - 1), help(n - 2) + nums[n])
            return dp[n]
        
        return help(len(nums) - 1)