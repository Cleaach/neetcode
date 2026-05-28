class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        smaller = self.subsets(nums[1:])
        
        smaller_with_first = [subset + [nums[0]] for subset in smaller]
        
        return smaller + smaller_with_first