class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i, sofar):
            if i == n:
                return 1 if sofar == target else 0

            if (i, sofar) in memo:
                return memo[(i, sofar)]

            memo[(i, sofar)] = (
                dfs(i + 1, sofar + nums[i]) +
                dfs(i + 1, sofar - nums[i])
            )

            return memo[(i, sofar)]

        return dfs(0, 0)