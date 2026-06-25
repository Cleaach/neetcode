class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        n = len(nums)
        for r in range(n):
            for l in range(r):
                res = max(res, sum(nums[l:r+1]))
        return res