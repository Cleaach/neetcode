class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        
        def dfs(i, j):
            # Base case: out of bounds or water
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 0
            
            # Mark as visited
            grid[i][j] = 0
            
            # Count this cell (1) + all connected cells
            area = 1
            area += dfs(i - 1, j)  # Up
            area += dfs(i + 1, j)  # Down
            area += dfs(i, j - 1)  # Left
            area += dfs(i, j + 1)  # Right
            
            return area
        
        # Find island starting from each unvisited land cell
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area