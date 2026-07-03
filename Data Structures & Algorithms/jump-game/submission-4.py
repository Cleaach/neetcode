"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [None for _ in nums]
        dp[0] = True

        def canReach(index):
            if dp[index] is None:
                for i in range(index - 1, -1, -1):
                    if nums[i] >= index - i:
                        if canReach(i):
                            dp[index] = True
                            return True
                dp[index] = False
                return False
            else:
                return dp[index]
            
        return canReach(len(nums) - 1)
"""
# GREEDY
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        