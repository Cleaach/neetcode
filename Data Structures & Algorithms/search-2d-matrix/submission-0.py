class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def access(index):
            return matrix[index // n][index % n]
        def help(left, right):
            if left > right:
                return False
            else:
                mid = (left + right) // 2
                if access(mid) > target:
                    return help(left, mid - 1)
                elif access(mid) < target:
                    return help(mid + 1, right)
                else:
                    return True
        return help(0, m * n - 1)