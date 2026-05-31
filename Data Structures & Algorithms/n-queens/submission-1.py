class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        diag1 = set()  # r - c (top-left to bottom-right)
        diag2 = set()  # r + c (top-right to bottom-left)
        
        def backtrack(row):
            # Base case: all queens placed
            if row == n:
                res.append([''.join(r) for r in board])
                return
            
            # Try placing queen in each column of current row
            for col in range(n):
                # Check if column or diagonals are attacked
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # Place queen
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Recurse to next row
                backtrack(row + 1)
                
                # Remove queen (backtrack)
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        backtrack(0)
        return res