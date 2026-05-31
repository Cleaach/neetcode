class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        def make(curr, i):
            if i == n:
                res.append(curr)
                return
            make(curr + [nums[i]], i + 1)
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            if j < n:
                make(curr, j)
            else:
                res.append(curr)
        
        make([], 0)
        return res

