class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        # initialize
        prefix[0] = height[0]
        suffix[n - 1] = height[n - 1]

        # build prefix max
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])

        # build suffix max
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])

        # compute result
        res = 0
        for i in range(n):
            res += min(prefix[i], suffix[i]) - height[i]

        return res