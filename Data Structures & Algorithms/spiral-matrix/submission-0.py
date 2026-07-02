class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []

        while len(res) < m * n:
            # traverse right along the top row
            if top <= bottom:
                for c in range(left, right + 1):
                    res.append(matrix[top][c])
                top += 1

            # traverse down along the right column
            if left <= right:
                for r in range(top, bottom + 1):
                    res.append(matrix[r][right])
                right -= 1

            # traverse left along the bottom row
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # traverse up along the left column
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res