class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, res = [num for num in nums], [num for num in nums], [num for num in nums]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        for j in range(1, len(nums) - 1):
            res[j] = prefix[j - 1] * suffix[j + 1]
        res[0] = suffix[1]
        res[-1] = prefix[-2]
        return res