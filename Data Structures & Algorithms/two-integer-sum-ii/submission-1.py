class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            d[numbers[i]] = i + 1
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in d:
                return [i + 1, d[complement]]