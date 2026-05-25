class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def help(left, right):
            print(left)
            print(right)
            if left > right:
                return -1
            elif left == right:
                if nums[left] == target:
                    return left
                else:
                    return -1
            else:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return help(mid + 1, right)
                else:
                    return help(left, mid - 1)
        
        return help(0, len(nums) - 1)