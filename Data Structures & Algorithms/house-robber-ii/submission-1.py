class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)

        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0], nums[1])

        withfirst = [-1 for _ in range(l)]
        withfirst[0] = nums[0]
        withfirst[1] = max(nums[0], nums[1])

        withoutfirst = [-1 for _ in range(l)]
        withoutfirst[1] = nums[1]
        withoutfirst[2] = max(nums[1], nums[2])
        
        def w(n):
            if withfirst[n] == -1:
                withfirst[n] = max(w(n - 1), w(n - 2) + nums[n])
            return withfirst[n]
        
        def wo(n):
            if withoutfirst[n] == -1:
                withoutfirst[n] = max(wo(n - 1), wo(n - 2) + nums[n])
            return withoutfirst[n]
        
        return max(w(l - 2), wo(l - 1))