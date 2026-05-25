class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def help(left, right):
            if left > right:
                return -1
            else:
                mid = (left + right) // 2
                if nums[mid] < target:
                    return help(mid + 1, right)
                elif nums[mid] > target:
                    return help(left, mid - 1)
                else:
                    return mid
        return help(0, len(nums) - 1)   