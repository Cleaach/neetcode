class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {};
        for i in nums:
            if (i in d):
                return True
            else:
                d[i] = i
        return False
