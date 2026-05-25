class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        res = 0
        for i in h:
            j = i
            if j - 1 not in h:
                length = 1
                while j + 1 in h:
                    length += 1
                    j += 1
                res = max(res, length)
        return res                