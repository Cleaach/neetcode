class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d.keys():
                return [d[nums[i]], i]
            if target - nums[i] in d.keys():
                return [d[target - nums[i]], i]
            d[nums[i]] = i
        return [0,0]

