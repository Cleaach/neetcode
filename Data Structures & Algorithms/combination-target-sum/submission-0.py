class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr, currTarget):
            # Base case: found valid combination
            if currTarget == 0:
                res.append(curr[:])  # Append copy
                return
            
            # Base case: exceeded target
            if currTarget < 0:
                return
            
            # Only iterate from 'start' onwards to avoid duplicates
            for i in range(start, len(nums)):
                num = nums[i]
                backtrack(i, curr + [num], currTarget - num)
        
        backtrack(0, [], target)
        return res