class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n^2)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        return False
                