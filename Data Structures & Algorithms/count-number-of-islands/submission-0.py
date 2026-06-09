class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        def bfs(i, j):
            if grid[i][j] == "s":
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "s"
            if i > 0:
                bfs(i - 1, j)
            if j > 0:
                bfs(i, j - 1)
            if i < rows - 1:
                bfs(i + 1, j)
            if j < cols - 1:
                bfs(i, j + 1)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    count += 1
        print(grid)
        return count

