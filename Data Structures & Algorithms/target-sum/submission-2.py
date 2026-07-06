class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dfs(i, sofar):
            if i == n and sofar == target:
                return 1
            if i == n:
                return 0
            return dfs(i + 1, sofar + nums[i]) + dfs(i + 1, sofar - nums[i])
        return dfs(0, 0)