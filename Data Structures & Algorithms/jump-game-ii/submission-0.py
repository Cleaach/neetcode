class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        # 1. Initialize with -1 so our memoization check actually works
        dp = [-1] * l 
        dp[-1] = 0

        def help(n):
            # Base Case: Reached the end
            if n >= l - 1:
                return 0
            # Return cached result if we've already calculated it
            if dp[n] != -1:
                return dp[n]
            
            # If we can reach the end in one jump from here
            if nums[n] + n >= l - 1:
                dp[n] = 1
                return 1
            
            res = float('inf')
            # 2. Fix the range to correctly iterate over all possible jumps
            # Cap it at 'l' to prevent looking outside the array boundaries
            max_jump = min(n + nums[n] + 1, l)
            for i in range(n + 1, max_jump):
                res = min(res, help(i) + 1)
                
            dp[n] = res
            return res
        
        return help(0)