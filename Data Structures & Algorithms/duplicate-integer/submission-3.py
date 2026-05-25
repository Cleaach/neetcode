class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) time, O(n) space
        h = dict()
        for i in nums:
            if i in h.keys():
                return True
            else:
                h[i] = "lol"
        return False
                