class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 0 0 -> 0 2
        # 0 1 -> 1 2
        # 0 2 -> 2 2
        # 1 0 -> 0 1
        # 1 1 -> 1 1
        # 1 2 -> 2 1
        # 2 0 -> 0 0
        # x y -> y n-x
        n = len(matrix)
        
        rotated = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated[j][n - 1 - i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]